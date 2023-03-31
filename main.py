# MAIN WINDOW FOR FITNESS APPLICATION

# Libraries and modules
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.uic import loadUi
import sys
# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    
    # Constructor for the main window
    def __init__(self):
        super().__init__()
    
        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.heihtDSB = self.lengthDoubleSpinBox
        self.weightDSB = self.weightDoubleSpinBox
        self.lPB = self.laskePushButton
        self.lPB.clicked.connect(self.calculateAll)
    # Define slots ie methods 
    def calculateAll(self):
        self.painoindexiLabel_2.setText('100')

if __name__ == "__main__":
    
    
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Create the mainwindow (and show it)
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())

   
    # Start the application