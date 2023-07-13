# decodigo.com
from tkinter import Tk, Label, Button, filedialog
import speech_recognition


class TranscribeAI:
    filePath = ""

    def __init__(self, master):
        master.geometry("400x300")
        master.resizable(False, False)

        self.master = master
        master.title("Transcribe AI")

        self.label = Label(master, text="Bienvenia a Transcribe AI")
        self.label.pack()

        self.label = Label(
            master,
            text="Selecciona un archivo en formato .wav \n y presiona el botón 'Enviar a Azure'",
        )
        self.label.pack()

        # Boton para seleccionar un archivo de audio
        self.openDocumentButton = Button(
            master, text="Seleccionar archivo", command=self.select_file
        )
        self.openDocumentButton.pack()

        self.documentSelected = Label(
            master, text=f"Archivo seleccionado: {TranscribeAI.filePath}"
        )
        self.documentSelected.pack()

        self.sendToAzureButton = Button(
            master, text="Enviar a Azure", state="disabled", command=self.send_to_azure
        )
        self.sendToAzureButton.pack()

        self.messages = Label(master, text="Esperando archivo...")
        self.messages.pack()

    def create_document_with_text(self, text):
        file_name = TranscribeAI.filePath.split(".")[0]
        file_name = file_name + ".txt"
        file = open(file_name, "w")
        file.write(text)
        file.close()

        self.messages.configure(text=f"Completado!!!!")

        TranscribeAI.filePath = ""
        self.sendToAzureButton.configure(state="disabled")
        self.documentSelected.configure(
            text=f"Archivo seleccionado: {TranscribeAI.filePath}"
        )

    def send_to_azure(self):
        self.messages.configure(text=f"Enviando y transcribiendo ...")
        result = speech_recognition.from_file(TranscribeAI.filePath)
        TranscribeAI.create_document_with_text(self, result)

    def select_file(self):
        TranscribeAI.filePath = filedialog.askopenfilename()

        self.documentSelected.configure(
            text=f"Archivo seleccionado: \n {TranscribeAI.filePath}"
        )
        self.messages.configure(text=f"Listo para Enviar a Azure")

        self.sendToAzureButton.configure(state="normal")


root = Tk()
miVentana = TranscribeAI(root)
root.mainloop()
