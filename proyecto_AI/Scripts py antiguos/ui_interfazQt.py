# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazQt.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#     QMetaObject, QObject, QPoint, QRect,
#     QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
#     QCursor, QFont, QFontDatabase, QGradient,
#     QIcon, QImage, QKeySequence, QLinearGradient,
#     QPainter, QPalette, QPixmap, QRadialGradient,
#     QTransform)
# from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPlainTextEdit,
#     QPushButton, QRadioButton, QSizePolicy, QWidget)
from PySide6.QtGui import *
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy, QWidget)
from PySide6.QtCore import *
class Ui_MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(784, 600)
        self.actionAccion = QAction(MainWindow)
        self.actionAccion.setObjectName(u"actionAccion")
        self.actionAccion.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frameRadiobuttons = QFrame(self.centralwidget)
        self.frameRadiobuttons.setObjectName(u"frameRadiobuttons")
        self.frameRadiobuttons.setGeometry(QRect(20, 260, 135, 100))
        self.frameRadiobuttons.setAutoFillBackground(False)
        self.frameRadiobuttons.setFrameShape(QFrame.Panel)
        self.frameRadiobuttons.setFrameShadow(QFrame.Raised)
        self.radioButton = QRadioButton(self.frameRadiobuttons)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 20, 101, 17))
        self.radioButton_2 = QRadioButton(self.frameRadiobuttons)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QRect(20, 60, 91, 17))
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setChecked(True)
        self.OkButton = QPushButton(self.centralwidget)
        self.OkButton.setObjectName(u"OkButton")
        self.OkButton.setGeometry(QRect(680, 190, 78, 24))
        self.textoEs = QPlainTextEdit(self.centralwidget)
        self.textoEs.setObjectName(u"textoEs")
        self.textoEs.setGeometry(QRect(20, 60, 331, 121))
        self.textoEs.setAutoFillBackground(False)
        self.textoEs.setFrameShape(QFrame.Box)
        self.textoEs.setFrameShadow(QFrame.Raised)
        self.textoEs.setLineWidth(1)
        self.textoEs.setMidLineWidth(2)
        self.textoEn = QPlainTextEdit(self.centralwidget)
        self.textoEn.setObjectName(u"textoEn")
        self.textoEn.setGeometry(QRect(430, 60, 331, 121))
        self.textoEn.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.textoEn.setFrameShape(QFrame.Box)
        self.textoEn.setFrameShadow(QFrame.Raised)
        self.textoEn.setMidLineWidth(2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.radioButton.show()
        self.radioButton_2.show()
        self.OkButton.show()
        self.textoEs.show()
        self.textoEn.show()
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAccion.setText(QCoreApplication.translate("MainWindow", u"Accion", None))
#if QT_CONFIG(tooltip)
        self.actionAccion.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Chequeado</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAccion.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"NO ONLINE", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"ONLINE", None))
        self.OkButton.setText(QCoreApplication.translate("MainWindow", u"Traducir", None))
    # retranslateUi
       

