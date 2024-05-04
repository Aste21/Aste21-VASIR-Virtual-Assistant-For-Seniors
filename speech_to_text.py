import whisper
import subprocess

def record_audio(duration=10):
    filename = "output.mp3"
    command = [
        "ffmpeg",
        "-f", "dshow",                      # Input format (DirectShow for Windows)
        "-i", "audio=@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\wave_{C25DFCAA-C0E2-4CBF-95F2-ABB236C85CF2}", # Specify the audio input device (Microphone)
        "-t", str(duration),                # Duration of recording
        #"-ac", "2",                         # Number of audio channels
        #"-ar", "44100",                     # Audio sampling rate
        #"-codec:a", "libmp3lame",           # MP3 audio codec
        filename                            # Output filename
    ]
    subprocess.run(command)
    return filename

def speech_to_text(filename):
    options = {'language': 'pl'}
    model = whisper.load_model("small")
    result = model.transcribe(filename, **options)
    return result["text"]

if __name__ == "__main__":
    mp3_filename = record_audio(10)
    text = speech_to_text(mp3_filename)
    print(text)

    

    


