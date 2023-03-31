# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys
from PyQt6 import QtCore # Core functionality of Qt
from PyQt6 import QtWidgets # UI elements functionality
from PyQt6.uic.load_ui import loadUi

# Class for the main window
class MainWindow(QtWidgets.QMainWindow):

    """MainWindow for the fitness app"""

    # Constructor for the main window
    def __init__(self):
        super().__init__()

        # Load the UI file
        loadUi('Main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.lPB = self.laskePushButton
        self.lPB.clicked.connect(self.calculateAll)

    # Define slots ie methods
    def calculateAll(self):
        self.painoindexiLabel_2.setText('100')

if __name__ == "__main__":
    # Create the application
    app = QtWidgets.QApplication(sys.argv)

    # Create the Main Window object from MainWindow class and show it on the screen
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())