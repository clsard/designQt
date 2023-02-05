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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(652, 723)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.textES = QTextEdit(Dialog)
        self.textES.setObjectName(u"textES")
        self.textES.setGeometry(QRect(30, 35, 590, 50))
        self.textES.setToolTipDuration(-1)
        self.textEN = QTextEdit(Dialog)
        self.textEN.setObjectName(u"textEN")
        self.textEN.setGeometry(QRect(30, 130, 590, 50))
        self.botonBorrar = QPushButton(Dialog)
        self.botonBorrar.setObjectName(u"botonBorrar")
        self.botonBorrar.setGeometry(QRect(30, 190, 121, 27))
        self.botonBorrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botonBorrar.setAutoFillBackground(False)
        self.botonSolicitar = QPushButton(Dialog)
        self.botonSolicitar.setObjectName(u"botonSolicitar")
        self.botonSolicitar.setGeometry(QRect(500, 230, 111, 27))
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
        self.radioOnLine = QRadioButton(self.groupBox)
        self.radioOnLine.setObjectName(u"radioOnLine")
        self.radioOnLine.setChecked(True)

        self.verticalLayout.addWidget(self.radioOnLine)

        self.radioOffLine = QRadioButton(self.groupBox)
        self.radioOffLine.setObjectName(u"radioOffLine")

        self.verticalLayout.addWidget(self.radioOffLine)

        self.botonTraducir = QPushButton(Dialog)
        self.botonTraducir.setObjectName(u"botonTraducir")
        self.botonTraducir.setEnabled(True)
        self.botonTraducir.setGeometry(QRect(500, 190, 111, 27))
        self.label_1 = QLabel(Dialog)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(200, 200, 256, 256))
        self.label_1.setFrameShape(QFrame.Box)
        self.label_1.setFrameShadow(QFrame.Raised)
        self.label_1.setLineWidth(3)
        self.label_1.setPixmap(QPixmap(u"G:/Mi unidad/piumosso.es/web/logo/logo nuevo 512x512.png"))
        self.label_1.setScaledContents(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(200, 460, 256, 256))
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setLineWidth(3)
        self.label_2.setPixmap(QPixmap(u"G:/Mi unidad/piumosso.es/web/logo/logo nuevo 512x512.png"))
        self.label_2.setScaledContents(True)
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 380, 121, 102))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cantidad_1 = QRadioButton(self.groupBox_2)
        self.cantidad_1.setObjectName(u"cantidad_1")
        self.cantidad_1.setChecked(True)

        self.verticalLayout_2.addWidget(self.cantidad_1)

        self.cantidad_2 = QRadioButton(self.groupBox_2)
        self.cantidad_2.setObjectName(u"cantidad_2")
        self.cantidad_2.setChecked(False)

        self.verticalLayout_2.addWidget(self.cantidad_2)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 500, 121, 141))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.size_1 = QRadioButton(self.groupBox_3)
        self.size_1.setObjectName(u"size_1")
        self.size_1.setChecked(True)

        self.verticalLayout_3.addWidget(self.size_1)

        self.size_2 = QRadioButton(self.groupBox_3)
        self.size_2.setObjectName(u"size_2")
        self.size_2.setChecked(False)

        self.verticalLayout_3.addWidget(self.size_2)

        self.size_3 = QRadioButton(self.groupBox_3)
        self.size_3.setObjectName(u"size_3")
        self.size_3.setChecked(False)

        self.verticalLayout_3.addWidget(self.size_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dall-e API", None))
#if QT_CONFIG(tooltip)
        self.textES.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.botonBorrar.setText(QCoreApplication.translate("Dialog", u"Borrar contenido", None))
        self.botonSolicitar.setText(QCoreApplication.translate("Dialog", u"Solicitar imagen", None))
        self.labelES.setText(QCoreApplication.translate("Dialog", u"Espa\u00f1ol", None))
        self.labelEN.setText(QCoreApplication.translate("Dialog", u"Ingl\u00e9s", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Traducci\u00f3n", None))
        self.radioOnLine.setText(QCoreApplication.translate("Dialog", u"On line", None))
        self.radioOffLine.setText(QCoreApplication.translate("Dialog", u"Solicitando", None))
        self.botonTraducir.setText(QCoreApplication.translate("Dialog", u"Traducir", None))
        self.label_1.setText("")
        self.label_2.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Cantidad", None))
        self.cantidad_1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.cantidad_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Tama\u00f1o", None))
        self.size_1.setText(QCoreApplication.translate("Dialog", u"256", None))
        self.size_2.setText(QCoreApplication.translate("Dialog", u"512", None))
        self.size_3.setText(QCoreApplication.translate("Dialog", u"1024", None))
    # retranslateUi

