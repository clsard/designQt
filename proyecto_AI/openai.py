import sys
from PySide6.QtWidgets import QMainWindow,QMessageBox, QApplication
from modulos.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # Crear la interfaz de usuario con Ui_Dialog
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
if __name__ == "__main__":
    app = QApplication()
    window = Ui_MainWindow()
    window.show()

    # Función (slot) al intentar cerrar la ventana del dialogo principal
    def on_window_close(event):
        result = QMessageBox.question(window, "Cerrar ventana", "¿Realmente quieres cerrar la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            #dialog.db.close()
            event.accept()
        else:
            event.ignore()

    # Dispara (Signal) del (slot) on_window_close) close. Evento del cierre de ventana (X) o Alt+F4
    window.closeEvent = on_window_close
    sys.exit(app.exec_())        