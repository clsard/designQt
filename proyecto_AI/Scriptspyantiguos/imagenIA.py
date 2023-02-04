# from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from modulos.ui_interfazQt import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets

import os
import openai
import base64
import time
import argparse
import sys

from dotenv import load_dotenv
from easygoogletranslate import EasyGoogleTranslate
translator= EasyGoogleTranslate(
  source_language = 'es',
  target_language = 'en',
  timeout = 10
)
load_dotenv()

""" class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # valorRadioButton = True
    # def __init__(self):
    #     super().__init__()
    #     self.setupUi(self)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.valorRadioButton = True
        self.OkButton.clicked.connect(self.button_ok_clicked)
        self.radioButton.clicked.connect(self.radioButton_clicked)
        self.radioButton_2.clicked.connect(self.radioButton_2_clicked)
app = QApplication(sys.argv) """
        
#############################################
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.valorRadioButton = True
        self.ui.OkButton.clicked.connect(self.button_ok_clicked)
        self.ui.radioButton.clicked.connect(self.radioButton_clicked)
        self.ui.radioButton_2.clicked.connect(self.radioButton_2_clicked)
    def button_ok_clicked(self):
        print("Button was clicked!")

    def radioButton_clicked(self):
        self.valorRadioButton = True
        print("Radio boton 1 clikeado")
        print(f"El valor del radio boton {self.valorRadioButton}")

    def radioButton_2_clicked(self):
        self.valorRadioButton = False
        print("Radio boton 2 clikeado")
        print(f"El valor del radio boton {self.valorRadioButton}")
app = QApplication(sys.argv)


#############################################


# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()
windows = Ui_MainWindow(app)
windows.show()
app.exec()




@@ -1,37 +1,73 @@
from PyQt6 import uic
# from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
 
from modulos.ui_prueba import *
from modulos.ui_interfazQt import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    valorRadioButton = True
import os
import openai
import base64
import time
import argparse
import sys

from dotenv import load_dotenv
from easygoogletranslate import EasyGoogleTranslate
translator= EasyGoogleTranslate(
  source_language = 'es',
  target_language = 'en',
  timeout = 10
)
load_dotenv()

""" class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # valorRadioButton = True
    # def __init__(self):
    #     super().__init__()
    #     self.setupUi(self)
    def __init__(self):
        super().__init__()
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.valorRadioButton = True
        self.OkButton.clicked.connect(self.button_ok_clicked)
        self.radioButton.clicked.connect(self.radioButton_clicked)
        self.radioButton_2.clicked.connect(self.radioButton_2_clicked)

app = QApplication(sys.argv) """
        

#############################################
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.valorRadioButton = True
        self.ui.OkButton.clicked.connect(self.button_ok_clicked)
        self.ui.radioButton.clicked.connect(self.radioButton_clicked)
        self.ui.radioButton_2.clicked.connect(self.radioButton_2_clicked)
    def button_ok_clicked(self):
        print("Button was clicked!")
    

    def radioButton_clicked(self):
        self.valorRadioButton = False
        self.valorRadioButton = True
        print("Radio boton 1 clikeado")
        print(f"El valor del radio boton {self.valorRadioButton}")

    def radioButton_2_clicked(self):
        self.valorRadioButton = True
        self.valorRadioButton = False
        print("Radio boton 2 clikeado")
        print(f"El valor del radio boton {self.valorRadioButton}")
app = QApplication(sys.argv)


#############################################


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()
windows = Ui_MainWindow(app)
windows.show()
app.exec()




