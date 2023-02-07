# César L Sard - 2023-02-03
# Desktop APP OpenAI - API
import os
import sys
import openai
import base64
import time
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from modulos.ui_dialog import Ui_Dialog
from PySide6.QtGui import QPixmap
from easygoogletranslate import EasyGoogleTranslate
from dotenv import load_dotenv
#from modulos.registroXML import Registro, GuardarXML
from modulos.registroDB import Database
class DialogWindow(QDialog):
    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)

        self.db = Database(host="localhost", user="clsard", password="*2013Cct&Clsm1205#", database="open_ai")

        self.mycursor = self.db.db_cursor

    def __del__(self):
        self.db.close()
        #self.mycursor.execute("SHOW DATABASES")

        # for x in mycursor:
        #     print(x)
        # db.close() 
        # sys.exit()
        
        # Crear la interfaz de usuario con Ui_Dialog
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # cargamos variables de entorno .env
        load_dotenv()
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
        self.ui.botonTraducir.setEnabled(False)
        self.ui.botonSolicitar.setEnabled(False)
        # Iniciamos cantidad de imagenes a 1
        self.cantidad = int(1)
        # Ocultamos label de la segunda imagen
        self.ui.label_2.setVisible(False)
        # Definimos tamaño de imagen por defecto a 256x256
        self.size_img = int(256)
        
        #si es True la traducción se realizará directamente
        self.trans_direct = True

        # Iniciamos parámetros para la traducción
        self.translator = EasyGoogleTranslate(
            source_language = 'es',
            target_language = 'en',
            timeout = 10
            )
        # Leemos la clave de la API de openAI    
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
    # Bloques de funciones (Slot) de los diferentes eventos (Signal)
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
        

    # Funcion (Slot) para traducir automáticamente el texto en textES
    def text_changed_online(self):
        if self.trans_direct and len(self.ui.textES.toPlainText()) > 0: # Si la variable que controla tipo de traduccion es True
            translation = self.translator.translate(self.ui.textES.toPlainText())
            self.ui.textEN.setText(translation)
            self.ui.botonSolicitar.setEnabled(True)
        # Si se ha borrado todo el texto en labelES borramos todo el texto en labelEN y desabilitamos botonSolicitar    
        elif len(self.ui.textES.toPlainText()) == 0:
            self.ui.textEN.setText("")
            self.ui.botonSolicitar.setEnabled(False)


        
    # Cualdo se solicita traducir a través del boton Traducir   (TRADUCCIÓN NO ONLINE)        
    def boton_traducir_click(self):
        if not self.trans_direct:  #Si es FALSO la Traduccion online (DIRECTA)
            translation = self.translator.translate(self.ui.textES.toPlainText())
            self.ui.textEN.setText(translation)
            if len(self.ui.textEN.toPlainText()) > 0:
                self.ui.botonSolicitar.setEnabled(True)
            else:
                self.ui.botonSolicitar.setEnabled(False)

    # Funcion (Slot) del botonBorrar
    def boton_borrar_click(self):
        resultado = QMessageBox.question(self, "Borrar contenido", "¿Realmente quiere borrar el contenido?",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resultado == QMessageBox.Yes:                    
            self.ui.textEN.setText("")
            self.ui.textES.setText("")
            self.ui.botonSolicitar.setEnabled(False)

   # Esta función (Slot) es la que solicita a openAI imagenen/es, segun el prompt obtenido de textEN    
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
        archivo_xml = "registrosDall-e.xml"
        carpeta_xml = "G:/Mi unidad/Dall-e/" + archivo_xml
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
                carpeta = "G:/Mi unidad/Dall-e/"
                filename = carpeta + imagen_name
                with open(filename, 'wb') as f:
                    # Se escribe la imagen en carpeta local Google G:/Mi unidad/Dall-e/
                    f.write(base64.urlsafe_b64decode(b64)) 

                    # Comenzamos proceso para visualizar imagenes en los label *********
                    pixmap = QPixmap(filename)
                    if i == int(0):
                        self.ui.label_1.setPixmap(pixmap)
                    elif i == int(1):
                        self.ui.label_2.setPixmap(pixmap)  
                    # Se termina proceso *********
                    
                    self.db.add_record("dall_e", fecha_bd, hora_bd, prompt_es, prompt_en, cantidad, size_solicitado, imagen_name ,carpeta_xml)
                    # guardar = GuardarXML(carpeta_xml)
                    # registro = Registro(fecha_actual, prompt_es, prompt_en, cantidad, size_solicitado, carpeta_xml, imagen_name)
                    # guardar.agregar_registro(registro)
                    
                    
                # guardar.guardar()




        except Exception as e:
            error_api = QMessageBox.question(self, "Error en main.py", f"Ha ocurrido un error: {e} en la petición",
                    QMessageBox.Yes , QMessageBox.Yes)
            print(f'Error: {e}')

        

        print(f"api key =  {openai.api_key}")
        print(f"Prompt =  {prompt_en}")


if __name__ == "__main__":
    app = QApplication()
    dialog = DialogWindow()
    dialog.show()
    app.exec()
