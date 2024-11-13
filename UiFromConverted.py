# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNETYSTÄ KÄYTTÖLITTYMÄTIEDOSTOSTA (MainWindow.py)
# ===================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääräykset
import sys # Käynistysargumentit

from PySide6 import QtWidgets #Qt-vimpaimet
from MainWindow import Ui_MainWindow # Käänetyn käyttöliitymän luokka

# Märitellään luokka, joka perii QMainWindow- ja UI_MainWindow luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""

    # Määritellään oliomuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.setupUi(self)

# Luodaan sovellus
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynistetään sovellus ja tapahtumienkäsittelijä
app.exec()
    
    