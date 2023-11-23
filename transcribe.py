import whisper
import subprocess

model = whisper.load_model("small")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("male.wav")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
file1 = open("result.txt","w")
file1.write(result.text)
file1.close()

prompt = result.text+"\nCreate notes from this text"

try:
    subprocess.run(["../llama.cpp/main", "-m", "../llama.cpp/models/llama-2-7b-chat.Q4_0.gguf", "-p", prompt, "-ngl", "128"])
except subprocess.CalledProcessError as e:
    print("error")
