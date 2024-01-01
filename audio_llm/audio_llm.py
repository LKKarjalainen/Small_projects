from ast import arg
import whisper
import subprocess
import sys
import wave
import math
import os
import argparse

def convert_to_wav(filename):
    wav_filename = filename.rsplit('.', 1)[0] + '.wav'
    subprocess.run(['ffmpeg', '-i', filename, wav_filename])
    return wav_filename

def transcribe_audio(file, output_file):
    if not file.endswith('.wav'):
        file = convert_to_wav(file)
    # print(file)
    print('Choose model size:')
    model_size = input()
    model = whisper.load_model(model_size)
    rawAudio = wave.open(file, 'rb')
    options = whisper.DecodingOptions()
    result = ""


    frameRate = rawAudio.getframerate()
    numFrames = rawAudio.getnframes()
    duration = numFrames/frameRate
    n_chunks = math.ceil(duration/30)
    frames_per_chunk = 30*frameRate

    chunks = []
    for i in range(0, n_chunks):
        start_index = i*frames_per_chunk
        rawAudio.setpos(start_index)
        frames = rawAudio.readframes(frames_per_chunk)
        
        chunk_filename = f'chunk{i}.wav'
        chunkpath = "chunks/"+chunk_filename
        with wave.open(chunkpath, 'wb') as chunk:
            chunk.setnchannels(rawAudio.getnchannels())
            chunk.setsampwidth(rawAudio.getsampwidth())
            chunk.setframerate(frameRate)
            chunk.writeframes(frames)
        chunks.append(os.path.abspath(chunkpath))

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

if mode == "transcribe":
    if not file.endswith('.txt'):
        transcribe_audio(file, output_file)
    else:
        print("File was a .txt file. Provide an audio file for transcription.")
elif mode == "prompt":
    result = open(file, "r").read()
    prompt = "[INST]\n"+args.prompt+"\n'"+result+"'\n[/INST]\n"
    try:
        subprocess.run(["../llama.cpp/main", "-m", path_to_llm, "-p", prompt, "-ngl", "128", "-c", "4000"])
    except subprocess.CalledProcessError as e:
        print("error")
elif mode == "both":
    if not file.endswith('.txt'):
        result = transcribe_audio(file, output_file)
    else:
        result = open(file, "r").read()

    prompt = "[INST]\n"+args.prompt+"\n'"+result+"'\n[/INST]\n"

    try:
        subprocess.run(["../llama.cpp/main", "-m", path_to_llm, "-p", prompt, "-ngl", "128", "-c", "4000"])
    except subprocess.CalledProcessError as e:
        print("error")
else:
    print("Mode not recognized.")
    print("Use one of the following: transcribe, prompt or both(Vram heavy)")
