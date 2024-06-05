import pyaudio
import numpy as np
import wave

class VoiceRecorder():
    def __init__(self):
        self.FORMAT = pyaudio.paInt16  # 16-bit resolution
        self.CHANNELS = 1  # Mono channel
        self.RATE = 44100  # 44.1kHz sampling rate
        self.CHUNK = 1024  # 1024 samples per frame
        self.SILENCE_THRESHOLD = 150  # Adjust the silence threshold (lower for more sensitivity)
        self.SILENCE_DURATION = 3  # Duration of silence in seconds to trigger stop
        self.DURATION = 0 # Duration without silence

    def close_recording(self, audio, stream):
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        audio.terminate()

    def save_the_file(self, filename, audio, frames):
        # Save the recorded data as a WAV file
        wf = wave.open(filename, "wb")
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(audio.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def record_audio(self, output_filename="output.wav", duration=10):
        # Create an interface to PortAudio
        audio = pyaudio.PyAudio()

        # Open a stream with the necessary parameters
        stream = audio.open(format=self.FORMAT, 
                        channels=self.CHANNELS, 
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        print(f"Recording for {duration} seconds...")

        frames = []

        # Record the audio in chunks
        for _ in range(0, int(self.RATE / self.CHUNK * duration)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        # Stop and close the stream
        self.close_recording(audio, stream)
        print(f"Recording finished. Saving to {output_filename}...")
        self.save_the_file(output_filename, audio, frames)
        print(f"File saved as {output_filename}.")

    def record_audio_with_silence_detection(self, output_filename="output.wav", silence_threshold=150, silence_duration=3):
        # Initialize pyaudio
        audio = pyaudio.PyAudio()
        # Start recording
        stream = audio.open(format=self.FORMAT, 
                            channels=self.CHANNELS, 
                            rate=self.RATE, 
                            input=True, 
                            frames_per_buffer=self.CHUNK)

        print("Recording...")

        frames = []
        silence_buffer = []  # Buffer to hold recent volume values
        max_silent_chunks = int(silence_duration * self.RATE / self.CHUNK)

        def calculate_rms(audio_data):
            """Calculate the root mean square (RMS) of the audio data."""
            return np.sqrt(np.mean(np.square(audio_data.astype(np.float64))))

        try:
            while True:
                data = stream.read(self.CHUNK)
                frames.append(data)
                # Convert the audio data to numpy array
                audio_data = np.frombuffer(data, dtype=np.int16)
                # Compute the volume (root mean square)
                volume = calculate_rms(audio_data)
                # Debug print for volume levels
                print(f"Volume: {volume}")
                # Add the current volume to the silence buffer
                silence_buffer.append(volume)
                # Maintain the buffer size to max_silent_chunks
                if len(silence_buffer) > max_silent_chunks:
                    silence_buffer.pop(0)
                # Check if all recent volumes in the buffer are below the silence threshold
                if len(silence_buffer) == max_silent_chunks and all(vol < silence_threshold for vol in silence_buffer):
                    print("Silence detected. Stopping recording.")
                    break
        except Exception as e:
            print(f"An error occurred: {e}")

        self.close_recording(audio, stream)
        self.save_the_file(output_filename, audio, frames)

        print(f"Recording saved as {output_filename}")