# HELP DIALOG WINDOW

# Libraries and mudules
import typing
from PyQt5 import QtCore, QtWidgets as QW
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class OpenHelp(QW.QDialog):
    def __init__(self):
        super().__init__()

        loadUi('ohjeDialog.ui', self)
        self.setWindowTitle('Kuntoilusovelluksen ohje')
        self.closePB = self.closePushButton
        self.closePB.clicked.connect(self.closeHelp)

    def closeHelp(self):
        self.close()