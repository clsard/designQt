# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        icon = QIcon()
        iconThemeName = u"applications-office"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        self.actionVer_solicitadas = QAction(MainWindow)
        self.actionVer_solicitadas.setObjectName(u"actionVer_solicitadas")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 140, 361, 71))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        self.menuIm_genes = QMenu(self.menubar)
        self.menuIm_genes.setObjectName(u"menuIm_genes")
        self.menuSolicitar = QMenu(self.menuIm_genes)
        self.menuSolicitar.setObjectName(u"menuSolicitar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuIm_genes.menuAction())
        self.menuIm_genes.addAction(self.menuSolicitar.menuAction())
        self.menuIm_genes.addSeparator()
        self.menuIm_genes.addAction(self.actionVer_solicitadas)
        self.menuSolicitar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Proyecto API openAI", None))
        self.actionVer_solicitadas.setText(QCoreApplication.translate("MainWindow", u"Ver solicitadas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Proyecto Open AI - API", None))
        self.menuIm_genes.setTitle(QCoreApplication.translate("MainWindow", u"Im\u00e1genes", None))
        self.menuSolicitar.setTitle(QCoreApplication.translate("MainWindow", u"Solicitar ", None))
    # retranslateUi

