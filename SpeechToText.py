import whisper

class SpeechToText():
    def __init__(self):
        self.model = whisper.load_model("small")
        self.language = 'Polish'
        self.fp16 = False
        #self.options = {'language': 'pl'}
    
    def transcribe(self, filename):
        result = self.model.transcribe(audio=filename, fp16=self.fp16, language = self.language)# **options)
        return result["text"]