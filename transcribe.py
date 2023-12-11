import whisper
import subprocess
import sys
import wave
import math
import io
import os
import mimetypes

def convert_to_wav(filename):
    wav_filename = filename.rsplit('.', 1)[0] + '.wav'
    subprocess.run(['ffmpeg', '-i', filename, wav_filename])
    return wav_filename

# TODO: split audio into 30-second chunks and transcribe each chunk.
# for amount of audio chunks in list: pad, mel (list), decode, write to result.txt.
if not sys.argv[2].endswith('.txt'):
    if not sys.argv[2].endswith('.wav'):
        sys.argv[2] = convert_to_wav(sys.argv[2])

    model = whisper.load_model(sys.argv[1])
    rawAudio = wave.open(sys.argv[2], 'rb')
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
        with wave.open(chunk_filename, 'wb') as chunk:
            chunk.setnchannels(rawAudio.getnchannels())
            chunk.setsampwidth(rawAudio.getsampwidth())
            chunk.setframerate(frameRate)
            chunk.writeframes(frames)
        
        chunks.append(os.path.abspath(chunk_filename))


    for chunk in chunks:
        audio = whisper.load_audio(chunk)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        _, probs = model.detect_language(mel)
        result += whisper.decode(model, mel, options).text


    # print the recognized text
    print(result)
    file1 = open("result.txt","w")
    file1.write(result)
    file1.close()
else:
    result = open(sys.argv[2], "r").read()

prompt = "Create bullet point notes from this text:\n'"+result+"'\n[end of text]\nBullet point notes:\n"

try:
    subprocess.run(["../llama.cpp/main", "-m", "../llama.cpp/models/llama-2-7b-chat.Q4_0.gguf", "-p", prompt, "-ngl", "128", "-c", "4000"])
except subprocess.CalledProcessError as e:
    print("error")
