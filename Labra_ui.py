# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Labra.ui'
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
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 340)
        MainWindow.setLocale(QLocale(QLocale.Finnish, QLocale.Finland))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ssnLineEdit = QLineEdit(self.centralwidget)
        self.ssnLineEdit.setObjectName(u"ssnLineEdit")
        self.ssnLineEdit.setGeometry(QRect(30, 40, 221, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(20)
        self.ssnLineEdit.setFont(font)
        self.ssnLineEdit.setToolTipDuration(3000)
        self.ssnLineEdit.setClearButtonEnabled(True)
        self.firstNameLineEdit = QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setGeometry(QRect(30, 110, 221, 31))
        self.firstNameLineEdit.setFont(font)
        self.lastNameLineEdit = QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setGeometry(QRect(270, 110, 221, 31))
        self.lastNameLineEdit.setFont(font)
        self.ssnLabel = QLabel(self.centralwidget)
        self.ssnLabel.setObjectName(u"ssnLabel")
        self.ssnLabel.setGeometry(QRect(30, 20, 91, 16))
        self.firstNameLabel = QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setGeometry(QRect(30, 90, 47, 13))
        self.lastNameLabel = QLabel(self.centralwidget)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setGeometry(QRect(270, 90, 47, 13))
        self.barcodeLabel = QLabel(self.centralwidget)
        self.barcodeLabel.setObjectName(u"barcodeLabel")
        self.barcodeLabel.setGeometry(QRect(30, 190, 221, 51))
        font1 = QFont()
        font1.setFamilies([u"Libre Barcode 128 Text"])
        font1.setPointSize(36)
        self.barcodeLabel.setFont(font1)
        self.printPushButton = QPushButton(self.centralwidget)
        self.printPushButton.setObjectName(u"printPushButton")
        self.printPushButton.setGeometry(QRect(360, 200, 131, 41))
        font2 = QFont()
        font2.setPointSize(18)
        self.printPushButton.setFont(font2)
        self.printPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.printPushButton.setStyleSheet(u"")
        self.amountSpinBox = QSpinBox(self.centralwidget)
        self.amountSpinBox.setObjectName(u"amountSpinBox")
        self.amountSpinBox.setGeometry(QRect(270, 200, 81, 41))
        font3 = QFont()
        font3.setPointSize(24)
        self.amountSpinBox.setFont(font3)
        self.amountSpinBox.setToolTipDuration(-1)
        self.amountSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.amountSpinBox.setMaximum(999)
        self.amountLabel = QLabel(self.centralwidget)
        self.amountLabel.setObjectName(u"amountLabel")
        self.amountLabel.setGeometry(QRect(270, 180, 111, 16))
        self.exampleStickerLabel = QLabel(self.centralwidget)
        self.exampleStickerLabel.setObjectName(u"exampleStickerLabel")
        self.exampleStickerLabel.setGeometry(QRect(30, 170, 91, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.ssnLineEdit, self.firstNameLineEdit)
        QWidget.setTabOrder(self.firstNameLineEdit, self.lastNameLineEdit)
        QWidget.setTabOrder(self.lastNameLineEdit, self.amountSpinBox)
        QWidget.setTabOrder(self.amountSpinBox, self.printPushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.ssnLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Suomalainen henkil\u00f6tunnus", None))
#endif // QT_CONFIG(tooltip)
        self.ssnLineEdit.setInputMask("")
        self.ssnLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"311259-123X", None))
        self.ssnLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.firstNameLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi", None))
        self.lastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
        self.barcodeLabel.setText(QCoreApplication.translate("MainWindow", u"ppkkvv-nnnv", None))
        self.printPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
#if QT_CONFIG(tooltip)
        self.amountSpinBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.amountLabel.setText(QCoreApplication.translate("MainWindow", u"Etikettien m\u00e4\u00e4r\u00e4", None))
        self.exampleStickerLabel.setText(QCoreApplication.translate("MainWindow", u"Mallietiketti", None))
    # retranslateUi

