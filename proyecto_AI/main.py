# César L Sard - 2023-02-03
# Desktop APP OpenAI - API
import os
import openai
import base64
import time
from PySide6.QtWidgets import QApplication, QPushButton, QDialog, QTextEdit, QDialogButtonBox, QMessageBox
from modulos.ui_dialog import Ui_Dialog
from easygoogletranslate import EasyGoogleTranslate
from dotenv import load_dotenv
class DialogWindow(QDialog):
    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)

        # Crear la interfaz de usuario con Ui_Dialog
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        load_dotenv()
        # Conectar la señal clicked de los radiobutton a una función
        self.ui.radioOnLine.clicked.connect(self.on_radio_clicked)
        self.ui.radioOffLine.clicked.connect(self.on_radio_clicked)
        self.ui.textES.textChanged.connect(self.text_changed_online)
        self.ui.botonTraducir.clicked.connect(self.boton_traducir_click)
        self.ui.botonBorrar.clicked.connect(self.boton_borrar_click)
        self.ui.botonSolicitar.clicked.connect(self.boton_solicitar_click)
        #Boton de traducción deshabilitado de comienzo
        #e iniciamos la variable trans_direc = False
        self.ui.botonTraducir.setEnabled(False)
        self.ui.botonSolicitar.setEnabled(False)

        #si es True la traducción se realizará directamente
        self.trans_direct = True

        self.translator = EasyGoogleTranslate(
            source_language = 'es',
            target_language = 'en',
            timeout = 10
            )
        openai.api_key = os.getenv("OPENAI_API_KEY")
        

    def on_radio_clicked(self):
        if self.ui.radioOnLine.isChecked():
            self.trans_direct = True
            self.ui.botonTraducir.setEnabled(False)
        else:
            self.trans_direct = False
            self.ui.botonTraducir.setEnabled(True)
        

        # Conectar la señal accepted del botón a una función
        # self.ui.buttonBox.accepted.connect(self.on_accepted)
        # self.ui.buttonBox.rejected.connect(self.on_rejected)

    #Funcion para transladar automáticamente el texto en ES
    def text_changed_online(self):
        if self.trans_direct and len(self.ui.textES.toPlainText()) > 0: # Si la variable que controla tipo de traduccion es True
            translation = self.translator.translate(self.ui.textES.toPlainText())
            self.ui.textEN.setText(translation)
            self.ui.botonSolicitar.setEnabled(True)
        elif len(self.ui.textES.toPlainText()) == 0:
            self.ui.textEN.setText("")
            self.ui.botonSolicitar.setEnabled(False)


        
    #Cualdo se solicita traducir a través del boton Traducir          
    def boton_traducir_click(self):
        if not self.trans_direct:  #Si es FALSO la Traduccion online
            translation = self.translator.translate(self.ui.textES.toPlainText())
            self.ui.textEN.setText(translation)
            if len(self.ui.textEN.toPlainText()) > 0:
                self.ui.botonSolicitar.setEnabled(True)
            else:
                self.ui.botonSolicitar.setEnabled(False)

    def boton_borrar_click(self):
        resultado = QMessageBox.question(self, "Borrar contenido", "¿Realmente quiere borrar el contenido?",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resultado == QMessageBox.Yes:                    
            self.ui.textEN.setText("")
            self.ui.textES.setText("")
            self.ui.botonSolicitar.setEnabled(False)
        
    def boton_solicitar_click(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        print(f"api key =  {openai.api_key}")
        pass        

    def on_accepted(self):
        # hacer algo cuando se pulse el botón OK
        pass

    def on_rejected(self):
        # hacer algo cuando se pulse el botón Cancelar
        pass



if __name__ == "__main__":
    app = QApplication()
    dialog = DialogWindow()
    dialog.show()
    app.exec()
