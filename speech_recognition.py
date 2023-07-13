import azure.cognitiveservices.speech as speech
import time
from tkinter import HORIZONTAL, VERTICAL, Frame, Scrollbar, Tk, Label, Text


def from_file(filepath):
    # Llamada a Azure
    speech_config = speech.SpeechConfig(
        subscription="8778e83e29594daa8666cf7d147d3c42",
        region="eastus",
        speech_recognition_language="es-ES",
    )
    audio_config = speech.audio.AudioConfig(filename=filepath)
    speech_recognizer = speech.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config
    )

    done = False
    textOut = ""

    def stop_cb(evt):
        print("CLOSING on {}".format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    str_newLine = " \n"

    def outPrint(evt):
        nonlocal textOut
        tmp_text = evt.result.text
        textOut += tmp_text + str_newLine
        print(tmp_text)

    speech_recognizer.recognized.connect(outPrint)
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.start_continuous_recognition()

    while not done:
        time.sleep(0.5)

    return textOut
    # return result.text
