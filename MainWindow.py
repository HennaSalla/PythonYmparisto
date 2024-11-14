# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object): 

    # Luodaan pääikkuna
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 1008)

        # Määritellään päävimpain, jonka sisälle muut vimpaimet sijoitetaan
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Määritellään käyttöliittymäelementit päävimpaimen sisälle
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 113, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 201, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 10, 75, 23))
        self.tulostaPushButton = QPushButton(self.centralwidget)
        self.tulostaPushButton.setObjectName(u"tulostaPushButton")
        self.tulostaPushButton.setGeometry(QRect(260, 10, 75, 23))

        # Tehdään oletusfontista poikeava fonttiasetus
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(10)
        font.setBold(False)

        # Käytetään fonttiasetusta painikkeessa
        self.tulostaPushButton.setFont(font)

        # Määritellään painikkeen tyyliasetukset
        self.tulostaPushButton.setStyleSheet(u"background-color: rgb(218, 145, 109);")

        # Asetetaan pääikkuna päävimpain
        MainWindow.setCentralWidget(self.centralwidget)

        # Määritellään valikko- ja tilarivit
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")

        # Luodaan tyhjä valikkorivi
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)

        # Luodaan tilari
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Kutsutaan metodia, joka muodostaa 8 bittiset elementtien nimet
        self.retranslateUi(MainWindow)

        # Määritellään singnaali, joka annetaan kuin tekstikenttää "lineEdit" muokataan 
        self.lineEdit.textChanged.connect(self.label.setText)

        QMetaObject.connectSlotsByName(MainWindow)

    # Metodi elementtien nimien muutamiskeis Unicode -> 8 bit
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tulostaPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))

