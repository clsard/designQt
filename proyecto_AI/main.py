 
from PySide6.QtWidgets import QApplication, QDialog, QTextEdit, QDialogButtonBox
from modulos.ui_dialog import Ui_Dialog

class DialogWindow(QDialog):
    def __init__(self, parent=None):
        super(DialogWindow, self).__init__(parent)

        # Crear la interfaz de usuario con Ui_Dialog
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Conectar la señal accepted del botón a una función
        # self.ui.buttonBox.accepted.connect(self.on_accepted)
        # self.ui.buttonBox.rejected.connect(self.on_rejected)
        self.ui.pushButton.setText("OKI")

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
    app.exec_()