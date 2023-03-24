# MAIN WINDOW FOR FITNESS APPLICATION

# Libraries and modules
from PyQt6 import QtCore # Core functionality of Qt
from PyQt6 import QtWidgets # UI elements functionality
from PyQt6.uic.load_ui import loadUi
import sys
# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    
    # Constructor for the main window
    def __init__(self):
        super().__init__()
    
        # Load the UI file
        self.main = loadUi('Main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.lPB = self.laskePushButton
        self.lPB.clicked.connect(self.calculateAll)
    # Define slots ie methods 
    def calculateAll(self):
        self.painoindexiLabel_2.setValue('100')

if __name__ == "__main__":
    
    
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Create the mainwindow (and show it)
    appWindow = MainWindow()
    appWindow.main.show()
    sys.exit(app.exec())

   
    # Start the application