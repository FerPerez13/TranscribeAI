import azure.cognitiveservices.speech as speech 

def from_file(filepath):
    speech_config = speech.SpeechConfig(subscription="8778e83e29594daa8666cf7d147d3c42", region="eastus", speech_recognition_language="es-ES")
    audio_config = speech.audio.AudioConfig(filename=filepath)
    speech_recognizer = speech.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_recognizer.recognize_once()
    #return result.json
    return result.text