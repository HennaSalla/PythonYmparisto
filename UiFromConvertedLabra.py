# LABORATORIOETIKETTISOVELLUKSEN PÄÄIKKUNAN
# LUOMINEN Labra_ui.py TIEDOSTON PERUSTEELLA
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets # Qt-vimpaimet
from Labra_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

import identityCheck2 # Henkilötunnuksen tarkistukseen liittyvät työkalut
import barcode # Viivakoodin muodostukseen tarvittavat rutiinit
from avtools import sound # Äänitoiminnot

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)
        self.ui.printPushButton.setEnabled(False)

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Kun poistutaan ssnLineEdit-elementistä suoritetaan barcodeLabel-elementin päivitys
        self.ui.ssnLineEdit.editingFinished.connect(self.updateBarcodeLabel)

        # Siistitään etunimi- ja sukunimielementit poistuttaessa:

        # Jokaisella elementillä oma siistintämetodi
        self.ui.firstNameLineEdit.editingFinished.connect(self.beautifyFirstName)

        """Signaali (connect) lähettää elementistä riippuen eri määrän dataa.
        Jos oma slot-metodi käyttää argumentteja, sen saama argumenttien määrä
        tai niiden tietotyypit ovat todennäköisesti väärin. Tästä syystä käytetään
        välittäjämetodia, joka lähettää varsinaiselle metodille oikean määrän argumentteja.
        Kun kutsutaan metodia, jolla ei ole argumentteja, ohjelma ei anna argumenttien
        tietotyyppi- tai määrävirhettä.
        """

        # Tehdään siistiminen välittäjämetodin interMediateSlot avulla:
        # self.ui.lastNameLineEdit.editingFinished.connect(self.interMediateSlot)

        """ Jos ei halua kirjoittaa välittäjämetodia, voi käyttää anonyymiä funktiota
        eli lambdaa, joka saa connect:n lähettämän datan, mutta lähettää varsinaiselle
        metodille (beautifyElement) oikean määrän (1) argumentteja. Huomaa, että lambda
        pitää pystyä kirjoittamaan yhdelle riville, jolloin siinä ei voi olla 
        ohjelmarakenteita mukana. Välittäjä metodissa niitä taas voidaan käyttää."""

        self.ui.lastNameLineEdit.editingFinished.connect(lambda: self.beautifyElement(self.ui.lastNameLineEdit))
        
        
        # Aktivoidaan tulostupainike sen jälkeen kun etikettien määrä on valittu
        self.ui.amountSpinBox.valueChanged.connect(self.enablePrintButton)
   
    # OHJELMOIDUT SLOTIT
    # ------------------

    # Viivakoodin muodostus ja barcodeLabel:n päivitys
    def updateBarcodeLabel(self):
        # Tarkistetaan, että henkilötunnus on oikein muodostettu
        uiSsn = self.ui.ssnLineEdit.text().upper() # Luetaan käyttöliittymästä henkilötunnus
        ssnToCheck = identityCheck2.NationalSSN(uiSsn) # Luodaan henkilötunnusobjekti
        self.ui.ssnLineEdit.setText(uiSsn) # Päivitetään myös syöttökenttä isoihin kirjaimiin

        # Jos se on oikein, luodaan viivakoodi
        if ssnToCheck.isValidSsn():
            barcode128 = barcode.Code128B(uiSsn) # Luodaan viivakoodi-olio
            barCodeToPrint = barcode128.buildBarcode() # Lisätään alku- ja loppumerkki sekä varmistussumma
            self.ui.barcodeLabel.setText(barCodeToPrint) # Päivitetään käyttöliittymän 
    
        # Jos se muodostettu väärin näytetään virheilmoitus MessageBox-ikkunassa
        else:
            self.errorTitle = 'Henkilötunnus virheellinen'
            self.errorText = ssnToCheck.errorMessage
            self.ui.ssnLineEdit.setFocus()
            self.openErrorMsgBox(self.errorTitle, self.errorText)
    
    # Siistitään etunimi muuttamalla alkukirjaimet isoiksi ja poistamalla ylim. välit
    def beautifyFirstName(self):
        elementText = self.ui.firstNameLineEdit.text()
        elementText = elementText.strip() # Poistetaan ylimääräiset välit tms
        elementText = elementText.title() # Muutetaan isot alkukirjaimet
        self.ui.firstNameLineEdit.setText(elementText) # Päivitetään elementti

    def beautifyLastName(self):
        elementText = self.ui.lastNameLineEdit.text()
        elementText = elementText.strip() # Poistetaan ylimääräiset välit tms
        elementText = elementText.title() # Muutetaan isot alkukirjaimet
        self.ui.lastNameLineEdit.setText(elementText) # Päivitetään elementti
    
    # Välittäjämetodi (agentti), joka ottaa vastaa signaalin ja sen mukana tulevat tiedot
    def interMediateSlot(self):

        # Asetetaan muokattava elementti ja kutsutaan varsinaista metodia, jolle annetaan täsmälleen 1 argumentti
        element = self.ui.lastNameLineEdit
        self.beautifyElement(element)


    # Yleispätevä elementin siistimismetodi, varsinainen metodi, jota interMediateSlot tai lambda kutsuu
    def beautifyElement(self, element):
        elementText = element.text()
        elementText = elementText.strip()
        elementText = elementText.title()
        element.setText(elementText)
    
    # Aktivoidaan tulostuspainike
    def enablePrintButton(self):
        if self.ui.ssnLineEdit.text != '' or self.ui.firstNameLineEdit.text != '' or self.ui.lastNameLineEdit != '':
            self.ui.printPushButton.setEnabled(True)


    # Virheilmoitusikkuna
    def openErrorMsgBox(self, errorTitle, errorText):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(errorTitle)
        msgBox.setText(errorText)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

    # TODO: Lisää tilariville tiedot asiakkaasta tyyliin
    # "Asiakas on 96 vuotias nainen"
if __name__ == "__main__":

    # Luodaan sovellus, jossa on käyttöjärjestelmästä riippumaton ulkonäkö (Fusion)
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä
    app.exec()
    