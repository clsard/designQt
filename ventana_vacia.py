import sys
from PypippQt6.QtWidgets import QApplication, QWidget

class VentanaVacia(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(50, 50, 500,350)
        self.setWindowTitle("Ventana Vacia")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    sys.exit(app.exec())