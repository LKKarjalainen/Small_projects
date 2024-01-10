import whisper
import subprocess
import sys
import wave
import math
import os
import argparse
from pydub import AudioSegment
from pydub.silence import detect_silence
import nvidia_smi
import tiktoken
from llama_cpp import Llama

argparser = argparse.ArgumentParser(description='Transcribes audio to text and integrates an llm for prompting the result.')
argparser.add_argument('-llm', '--language-model', dest="llm", default="../llama.cpp/models/llama-2-7b-chat.Q4_0.gguf", type=str, help="Path to language model to use. Must be compatible with llama.cpp")
argparser.add_argument('-p', '--prompt', dest="prompt", default="Create numerous bullet point notes from this text:", type=str, help="Prompt the llm with the transcribtion as the source.")
argparser.add_argument('-m', '--mode', dest="mode", default="both", type=str, help='Mode of audio_llm.py. Transcribe or prompt result or both.')
argparser.add_argument('-f', '--file', dest="file", default="result.txt", type=str, help='Input file. Audio or .txt')
argparser.add_argument('-o', '--output', dest="output", default="result.txt", type=str, help='Specify the output file of the transcription.')

args = argparser.parse_args()
# print(args)

file = args.file
mode = args.mode
output_file = args.output
path_to_llm = args.llm

def convert_to_wav(filename):
    wav_filename = filename.rsplit('.', 1)[0] + '.wav'
    subprocess.run(['ffmpeg', '-i', filename, wav_filename])
    return wav_filename

def transcribe_audio(file, output_file):
    if not file.endswith('.wav'):
        file = convert_to_wav(file)
    # print(file)
    model_size = input('Choose model size: ')
    if model_size == "small" or model_size == "medium" or model_size == "large" or model_size == "base" or model_size == "tiny":
        model = whisper.load_model(model_size)
    else:
        print("Model size not recognized.")
        sys.exit()
    rawAudio = wave.open(file, 'rb')
    options = whisper.DecodingOptions()
    result = ""

    split_method = input("Split audio by silence? (Y/n): ")
    chunks = []

    if split_method == "y" or split_method == "Y":
        # Get the silent portions of the audio.
        audio_seg = AudioSegment.from_wav(file)

        # Super slow.
        silent_ranges = detect_silence(audio_seg, min_silence_len=150, silence_thresh=-60)
        last_silences = []
        j = 1
        for i in range(0, len(silent_ranges)):
            if silent_ranges[i][0] > 30000*j:
                last_silences.append(silent_ranges[i-1])
                j += 1
        
        # Get the chunks of audio to transcribe.
        audio_chunks = []
        audio_chunks.append(audio_seg[0:last_silences[0][0]+50])
        for i in range(0, len(last_silences)-1):
            print(last_silences[i])
            audio_chunks.append(audio_seg[last_silences[i][1]-10:last_silences[i+1][0]+10])
        audio_chunks.append(audio_seg[last_silences[len(last_silences)-1][1]-10:-1])
        
        # Export audio_chunks to wav files.
        for i in range(0, len(audio_chunks)):
            chunk_filename = f'audio_chunk{i}.wav'
            chunkpath = "chunks/"+chunk_filename
            audio_chunks[i].export(chunkpath, format="wav")
            chunks.append(os.path.abspath(chunkpath))

    elif split_method == "n" or split_method == "N":
        frameRate = rawAudio.getframerate()
        numFrames = rawAudio.getnframes()
        duration = numFrames/frameRate
        n_chunks = math.ceil(duration/30)
        frames_per_chunk = 30*frameRate

        for i in range(0, n_chunks):
            start_index = i*frames_per_chunk
            rawAudio.setpos(start_index)
            frames = rawAudio.readframes(frames_per_chunk)
            
            chunk_filename = f'audio_chunk{i}.wav'
            chunkpath = "chunks/"+chunk_filename
            with wave.open(chunkpath, 'wb') as chunk:
                chunk.setnchannels(rawAudio.getnchannels())
                chunk.setsampwidth(rawAudio.getsampwidth())
                chunk.setframerate(frameRate)
                chunk.writeframes(frames)
            chunks.append(os.path.abspath(chunkpath))
    else:
        print("Split method not recognized.")
        sys.exit()

    # Transcribe audio chunks sequentially.
    i = 1
    for chunk in chunks:
            audio = whisper.load_audio(chunk)
            audio = whisper.pad_or_trim(audio)
            if model_size == "large":
                mel = whisper.log_mel_spectrogram(audio=audio, n_mels=128).to(model.device)
            else:
                mel = whisper.log_mel_spectrogram(audio).to(model.device)
            _, probs = model.detect_language(mel)
            result += whisper.decode(model, mel, options).text
            result += " "
            print(i, "/", len(chunks), "of audio transcribed.")
            i += 1

    # print the recognized audio
    print(result)
    file1 = open(output_file,"w")
    file1.write(result)
    file1.close()
    return result

def prompt_llm(prompt, path_to_llm):
    nvidia_smi.nvmlInit()
    Vram_info = nvidia_smi.nvmlDeviceGetMemoryInfo(nvidia_smi.nvmlDeviceGetHandleByIndex(0))
    nvidia_smi.nvmlShutdown()
    free_vram = Vram_info.free

    print("Total VRAM:", Vram_info.total)
    print("Free VRAM:", free_vram)
    print("Used VRAM:", Vram_info.used)

    llm_size = float(input("Input llm size in billions: ").strip() or "7")
    llm_quantization = float(input("Input llm quantization: ").strip() or "4")
    llm_layers = float(input("Input llm layers: ").strip() or "32")
    llm_embedding_dimensions = float(input("Input llm embedding dimensions: ").strip() or "4096")
    llm_max_context_tokens = float(input("Input llm maximum context size in tokens: ").strip() or "4096")
    llm_vram_usage = (llm_size*2/llm_quantization+0.1)*1024**3
    print(f"Model vram usage: {llm_vram_usage} bytes or {llm_vram_usage/1024**3} GB")

    if llm_vram_usage > free_vram:
        print("Not enough VRAM for this model.")
        sys.exit()

    vram_for_prompt = free_vram-llm_vram_usage
    print(f"Free VRAM for prompt: {vram_for_prompt} bytes or {vram_for_prompt/1024**3} GB")
    llm_max_prompt_vram = llm_layers*llm_max_context_tokens*llm_embedding_dimensions*4+(300*1024**2)
    # print(f"Max prompt vram: {llm_max_prompt_vram} bytes or {llm_max_prompt_vram/1024/1024/1024} GB")

    # Calculate max prompt tokens for available vram (vram_for_prompt).
    if llm_max_prompt_vram > vram_for_prompt:
        prompt_vram_budget = vram_for_prompt - (300*1024**2)
        print(f"KV vram budget: {prompt_vram_budget} bytes or {prompt_vram_budget/1024/1024} MB")
        prompt_token_budget = (prompt_vram_budget / (llm_layers*llm_embedding_dimensions*4)) - 4
        print(f"Max prompt tokens: {prompt_token_budget}")
    else:
        prompt_token_budget = llm_max_context_tokens-4
        print(f"Max prompt tokens: {prompt_token_budget}")
    prompt_word_budget = prompt_token_budget*3/4
    # Estimate words and tokens in prompt.
    words_in_prompt = len(prompt.split())

    enc = tiktoken.get_encoding("gpt2")
    tokens = enc.encode(prompt)

    tokens_in_prompt = len(tokens)
    print(f"Words and tokens in prompt: {words_in_prompt} and {tokens_in_prompt}")

    prompt_chunks = []


    # Split prompt into chunks of max_prompt_words words.
    if tokens_in_prompt > prompt_token_budget:
        print(f"Splitting prompt into chunks of {prompt_token_budget} tokens.")
        current_token_chunk = []
        for token in tokens:
            if len(current_token_chunk) < prompt_token_budget:
                current_token_chunk.append(token)
            else:
                prompt_chunks.append(current_token_chunk)
                current_token_chunk = []
        prompt_chunks.append(current_token_chunk)
        """ prompt_words = prompt.split()
        current_chunk = ""
        for word in prompt_words:
            if len(current_chunk.split()) < prompt_word_budget:
                current_chunk += word+" "
            else:
                prompt_chunks.append(current_chunk)
                current_chunk = ""
        prompt_chunks.append(current_chunk) """
    else:
        prompt_chunks.append(tokens)
    prompt_chunks = enc.decode_batch(prompt_chunks)
    """ for chunk in prompt_chunks:
        print(chunk+"\n\n") """

    # print(prompt_chunks)
    outputs = []
    LLM =  Llama(model_path=path_to_llm, n_ctx=4096, n_gpu_layers=128, verbose=False)
    for chunk in prompt_chunks:
        # print(len(chunk.split()))
        output = LLM("[INST]\n"+args.prompt+f"'{chunk}'\n[/INST]\n", max_tokens=1000)
        # print(output["choices"][0]["text"])
        outputs.append(output)
        """ try:
            subprocess.run(["../llama.cpp/main", "-m", path_to_llm, "-p", "[INST]\n"+args.prompt+f"'{chunk}'\n[/INST]\n", "-ngl", "128", "-c", "4096"])
        except subprocess.CalledProcessError as e:
            print("error")
            print(e.output) """
    
    for output in outputs:
        print(output["choices"][0]["text"])



if mode == "transcribe":
    if not file.endswith('.txt'):
        transcribe_audio(file, output_file)
    else:
        print("File was a .txt file. Provide an audio file for transcription.")

elif mode == "prompt":
    if not file.endswith('.txt'):
        result = transcribe_audio(file, output_file)
    else:
        result = open(file, "r").read()

    prompt = f"'{result}'\n[/INST]\n"
    
    prompt_llm(prompt, path_to_llm)

# Sort of useless.
elif mode == "both":
    if not file.endswith('.txt'):
        result = transcribe_audio(file, output_file)
    else:
        result = open(file, "r").read()

    prompt = "[INST]\n"+args.prompt+"\n'"+result+"'\n"

    prompt_llm(prompt, path_to_llm)

else:
    print("Mode not recognized.")
    print("Use one of the following: transcribe, prompt or both(Vram heavy)")
