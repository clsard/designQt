# César L Sard - 2023-02-03
# Desktop APP OpenAI - API - Dall-e
import os
import openai
import base64
import time
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from modulos.ui_dialog import Ui_Dialog
from PySide6.QtGui import QPixmap
from easygoogletranslate import EasyGoogleTranslate
from dotenv import load_dotenv
from modulos.registroDB import Database

class DialogWindow(QDialog):
    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)
        # cargamos variables de entorno .env
        load_dotenv() 
        # Leemos la clave de acceso a la Base de Datos    
        mi_clave = os.getenv("BASEDATOS_PASSWORD")
        
        self.db = Database(host="localhost", user="clsard", password=mi_clave, database="open_ai")

        # Crear la interfaz de usuario con Ui_Dialog
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Conectar eventos (Signal) a una función (Slot)
        
        self.ui.radioOnLine.clicked.connect(self.on_radio_clicked)
        self.ui.radioOffLine.clicked.connect(self.on_radio_clicked)
        self.ui.cantidad_1.clicked.connect(self.cantidad_clicked)
        self.ui.cantidad_2.clicked.connect(self.cantidad_clicked)
        self.ui.size_1.clicked.connect(self.size_clicked)
        self.ui.size_2.clicked.connect(self.size_clicked)
        self.ui.size_3.clicked.connect(self.size_clicked)
        self.ui.textES.textChanged.connect(self.text_changed_online)
        self.ui.botonTraducir.clicked.connect(self.boton_traducir_click)
        self.ui.botonBorrar.clicked.connect(self.boton_borrar_click)
        self.ui.botonSolicitar.clicked.connect(self.boton_solicitar_click)
        
        # Boton de traducción y solicitud deshabilitado de comienzo
        self.ui.botonTraducir.setEnabled(True)
        self.ui.botonSolicitar.setEnabled(False)
        self.ui.radioOffLine.setChecked(True)
        # Iniciamos cantidad de imagenes a 1
        self.cantidad = int(1)
        # Ocultamos label de la segunda imagen
        self.ui.label_2.setVisible(False)
        # Definimos tamaño de imagen por defecto a 256x256
        self.size_img = int(256)
        #si es True la traducción se realizará directamente
        self.trans_direct = False

        # Iniciamos parámetros para la traducción
        self.translator = EasyGoogleTranslate(
            source_language = 'es',
            target_language = 'en',
            timeout = 10
            )
    
    # Radiobuttons cliqueados. Bloques de funciones (Slot) de los diferentes eventos (Signal)
    def on_radio_clicked(self):
        if self.ui.radioOnLine.isChecked():
            self.trans_direct = True
            self.ui.botonTraducir.setEnabled(False)
        else:
            self.trans_direct = False
            self.ui.botonTraducir.setEnabled(True)
    def cantidad_clicked(self):    
        if self.ui.cantidad_1.isChecked():
            self.cantidad = int(1)
            self.ui.label_2.setVisible(False)
        else:
            self.cantidad = int(2)
            self.ui.label_2.setVisible(True)
        print (f"la cantidad de imagenes solicitadas es: {self.cantidad}")
    def size_clicked(self):
        if self.ui.size_2.isChecked():
            self.size_img = int(512)
        elif self.ui.size_3.isChecked():
            self.size_img = int(1024)
        else:
            self.size_img = int(256)
        print (f"el tamaño de imagen seleccionado es: {self.size_img}")
        

    # Introduciendo texto español. Funcion (Slot) para traducir automáticamente el texto en textES
    def text_changed_online(self):
        if self.trans_direct and len(self.ui.textES.toPlainText()) > 0: # Si la variable que controla tipo de traduccion es True
            translation = self.translator.translate(self.ui.textES.toPlainText())
            self.ui.textEN.setText(translation)
            self.ui.botonSolicitar.setEnabled(True)
        # Si se ha borrado todo el texto en labelES borramos todo el texto en labelEN y desabilitamos botonSolicitar    
        elif len(self.ui.textES.toPlainText()) == 0:
            self.ui.textEN.setText("")
            self.ui.botonSolicitar.setEnabled(False)


        
    # Boton Traducir (Slot) Cuando se solicita traducir   (TRADUCCIÓN NO ONLINE)        
    def boton_traducir_click(self):
        if not self.trans_direct:  #Si es FALSO la Traduccion online (DIRECTA)
            translation = self.translator.translate(self.ui.textES.toPlainText())
            self.ui.textEN.setText(translation)
            if len(self.ui.textEN.toPlainText()) > 0:
                self.ui.botonSolicitar.setEnabled(True)
            else:
                self.ui.botonSolicitar.setEnabled(False)

    # Boton de Borrado de texto: Funcion (Slot)
    def boton_borrar_click(self):
        resultado = QMessageBox.question(self, "Borrar contenido", "¿Realmente quiere borrar el contenido?",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resultado == QMessageBox.Yes:                    
            self.ui.textEN.setText("")
            self.ui.textES.setText("")
            self.ui.botonSolicitar.setEnabled(False)

   # Boton Solicitar: función (Slot) es la que solicita a openAI imagenen/es, segun el prompt obtenido de textEN    
    def boton_solicitar_click(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        prompt_en = self.ui.textEN.toPlainText()
        prompt_es = self.ui.textES.toPlainText() # Para guardar en archivo XML
        
        #sys.exit("salida forzada")
        res = openai.Image.create(
            prompt=prompt_en,
            n=int(self.cantidad),
            size=f'{self.size_img}x{self.size_img}',
            response_format="b64_json"
        )
        cantidad = self.cantidad
        carpeta_img = "G:/Mi unidad/Dall-e/"
        size_solicitado = self.size_img
        try:
            # Borramos consola
            os.system('clear')
            
            # Bucle donde se guardan las imagenes en local y se visualizan imagenes
            for i in range(0, len(res['data'])):
                b64 = res['data'][i]['b64_json']

                fecha_bd = time.strftime("%Y%m%d")
                hora_bd = (time.strftime("%H%M%S"))
                fecha_actual = f"{fecha_bd}-{hora_bd}"
                
                imagen_name = fecha_actual + f"-{prompt_en[:8]}0" + str(i) + ".png"
                filename = "Proyecto_AI/imagenes/" + imagen_name
                print('Saving file ' + filename)
                with open(filename, 'wb') as f:
                    # Se escribe la imagen en carpeta local Proyecto_AI/imagenes/
                    f.write(base64.urlsafe_b64decode(b64))
                #carpeta = "G:/Mi unidad/Dall-e/"
                filename = carpeta_img + imagen_name
                
                with open(filename, 'wb') as f:
                    # Se escribe la imagen en carpeta local Google G:/Mi unidad/Dall-e/
                    f.write(base64.urlsafe_b64decode(b64)) 

                    # Comenzamos proceso para visualizar imagenes en los label y guardar registros*********
                    pixmap = QPixmap(filename)
                    if i == int(0):
                        self.ui.label_1.setPixmap(pixmap)
                    elif i == int(1):
                        self.ui.label_2.setPixmap(pixmap)  
                    
                    carpeta_img = filename
                    self.db.add_record_img("dall_e", fecha_bd, hora_bd, prompt_es, prompt_en, cantidad, size_solicitado, imagen_name ,carpeta_img)
                    # Se reinicia a su valor por defecto la carpeta local
                    carpeta_img = "G:/Mi unidad/Dall-e/"
                    # Se termina proceso *********
      




        except Exception as e:
            error_api = QMessageBox.question(self, "Error en main.py", f"Ha ocurrido un error: {e} en la petición",
                    QMessageBox.Yes , QMessageBox.Yes)
            print(f'Error: {e}')



if __name__ == "__main__":
    app = QApplication()
    dialog = DialogWindow()
    dialog.show()

    # Función (slot) al intentar cerrar la ventana del dialogo principal
    def on_window_close(event):
        result = QMessageBox.question(dialog, "Cerrar ventana", "¿Realmente quieres cerrar la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            dialog.db.close()
            event.accept()
        else:
            event.ignore()

    # Dispara (Signal) del (slot) on_window_close) close. Evento del cierre de ventana (X) o Alt+F4
    dialog.closeEvent = on_window_close
    app.exec()
