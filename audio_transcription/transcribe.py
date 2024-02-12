import whisper
import subprocess
import sys
import wave
import math
import os
import argparse
from pydub import AudioSegment
from pydub.silence import detect_silence

argparser = argparse.ArgumentParser(description='Transcribes audio to text based on silence or length')
argparser.add_argument('-f', '--file', dest="file", default="audio.txt", type=str, help='Input file. Audio or .txt')
argparser.add_argument('-o', '--output', dest="output", default="result.txt", type=str, help='Specify the output file of the transcription.')

args = argparser.parse_args()
# print(args)

file = args.file
output_file = args.output

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

    split_method = input("Split audio on silence? (Y/n): ")

    chunks = []
    if split_method == "y" or split_method == "Y":
        audio_seg = AudioSegment.from_wav(file)

        # Super slow.
        silent_ranges = detect_silence(audio_seg, min_silence_len=150, silence_thresh=-60)
        split_points = []
        j = 1
        for i in range(0, len(silent_ranges)):
            if silent_ranges[i][0] > 30000*j:
                split_points.append(silent_ranges[i-1])
                j += 1

        # Get the chunks of audio to transcribe.
        audio_chunks = []
        audio_chunks.append(audio_seg[0:split_points[0][0]+50])
        for i in range(0, len(split_points)-1):
            # print(last_silences[i])
            start_point = split_points[i][1]-10
            end_point = split_points[i+1][0]+10
            audio_chunks.append(audio_seg[start_point:end_point])
        audio_chunks.append(audio_seg[split_points[len(split_points)-1][1]-10:-1])

        # Export audio_chunks to wav files.
        for i in range(0, len(audio_chunks)):
            chunk_filename = f'audio_chunk{i}.wav'
            chunkpath = "chunks/"+chunk_filename
            audio_chunks[i].export(chunkpath, format="wav")
            chunks.append(os.path.abspath(chunkpath))

    elif split_method == "n" or split_method == "N":
        rawAudio = wave.open(file, 'rb')
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
    whisper_options = whisper.DecodingOptions()
    file = open(output_file,"w")
    result = ""
    i = 1
    for chunk in chunks:
            audio = whisper.load_audio(chunk)
            audio = whisper.pad_or_trim(audio)
            if model_size == "large":
                mel = whisper.log_mel_spectrogram(audio=audio, n_mels=128).to(model.device)
            else:
                mel = whisper.log_mel_spectrogram(audio).to(model.device)
            _, probs = model.detect_language(mel)
            result = whisper.decode(model, mel, whisper_options).text + " "
            print(i, "/", len(chunks), "of audio transcribed.")
            file.write(result)
            i += 1

    file.close()

if __name__ == "__main__":
    transcribe_audio(file, output_file)
    print("Transcription complete.")