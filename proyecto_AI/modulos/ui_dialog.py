# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView, QGroupBox,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(652, 527)
        Dialog.setAutoFillBackground(False)
        self.textES = QTextEdit(Dialog)
        self.textES.setObjectName(u"textES")
        self.textES.setGeometry(QRect(30, 35, 590, 50))
        self.textEN = QTextEdit(Dialog)
        self.textEN.setObjectName(u"textEN")
        self.textEN.setGeometry(QRect(30, 130, 590, 50))
        self.botonBorrar = QPushButton(Dialog)
        self.botonBorrar.setObjectName(u"botonBorrar")
        self.botonBorrar.setGeometry(QRect(30, 190, 121, 27))
        self.botonBorrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonSolicitar = QPushButton(Dialog)
        self.botonSolicitar.setObjectName(u"botonSolicitar")
        self.botonSolicitar.setGeometry(QRect(500, 450, 111, 27))
        self.labelES = QLabel(Dialog)
        self.labelES.setObjectName(u"labelES")
        self.labelES.setGeometry(QRect(30, 10, 56, 19))
        self.labelEN = QLabel(Dialog)
        self.labelEN.setObjectName(u"labelEN")
        self.labelEN.setGeometry(QRect(30, 100, 56, 19))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 240, 121, 102))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioSolicitando = QRadioButton(self.groupBox)
        self.radioSolicitando.setObjectName(u"radioSolicitando")

        self.verticalLayout.addWidget(self.radioSolicitando)

        self.radioOnLine = QRadioButton(self.groupBox)
        self.radioOnLine.setObjectName(u"radioOnLine")
        self.radioOnLine.setChecked(True)

        self.verticalLayout.addWidget(self.radioOnLine)

        self.botonTraducir = QPushButton(Dialog)
        self.botonTraducir.setObjectName(u"botonTraducir")
        self.botonTraducir.setEnabled(True)
        self.botonTraducir.setGeometry(QRect(500, 190, 111, 27))
        self.imagenView = QGraphicsView(Dialog)
        self.imagenView.setObjectName(u"imagenView")
        self.imagenView.setGeometry(QRect(190, 230, 256, 256))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dall-e API", None))
        self.botonBorrar.setText(QCoreApplication.translate("Dialog", u"Borrar contenido", None))
        self.botonSolicitar.setText(QCoreApplication.translate("Dialog", u"Solicitar imagen", None))
        self.labelES.setText(QCoreApplication.translate("Dialog", u"Espa\u00f1ol", None))
        self.labelEN.setText(QCoreApplication.translate("Dialog", u"Ingl\u00e9s", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Traducci\u00f3n", None))
        self.radioSolicitando.setText(QCoreApplication.translate("Dialog", u"Solicitando", None))
        self.radioOnLine.setText(QCoreApplication.translate("Dialog", u"On line", None))
        self.botonTraducir.setText(QCoreApplication.translate("Dialog", u"Traducir", None))
    # retranslateUi

