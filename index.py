import whisper
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

logging.info("Loading model...")
model = whisper.load_model("turbo")

logging.info("Loading and processing audio...")
# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("voice.mp3")
audio = whisper.pad_or_trim(audio)

logging.info("Creating log-Mel spectrogram...")
# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

logging.info("Detecting spoken language...")
# detect the spoken language
_, probs = model.detect_language(mel)
detected_language = max(probs, key=probs.get)
logging.info(f"Detected language: {detected_language}")

logging.info("Decoding the audio...")
# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
logging.info("Transcription complete.")
print(result.text)

# Write the result to a text file
with open("transcription.txt", "w") as file:
    file.write(result.text)
logging.info("Transcription written to transcription.txt")