# MAIN WINDOW FOR FITNESS APPLICATION

# Libraries and modules
import sys
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets # UI elements functionality
from PyQt5.uic import loadUi # reads the Ui file
import kuntoilija
import timetools
# Class for the main window
class MainWindow(QtWidgets.QMainWindow):
    
    # Constructor for the main window
    def __init__(self):
        super().__init__()
    
        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.heightDSB = self.lengthDoubleSpinBox
        self.weightDSB = self.weightDoubleSpinBox
        self.nameLE = self.nameLineEdit
        self.birthDE = self.birthDateEdit
        self.genderCB = self.genderComboBox
        self.wDE = self.weighingDateEdit
        self.wDE.setDate(QtCore.QDate.currentDate()) # Set the weighing date to the current date
        self.kaulaSB = self.kaulaSpinBox
        self.vuotaroSB = self.vyotaroSpinBox
        self.lantioSB = self.lantioSpinBox
        
        self.lPB = self.laskePushButton
        self.lPB.clicked.connect(self.calculateAll)
        
        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveData)
        self.savePB.setEnabled(False)
        
      
    # Define slots ie methods 
    
    # Calculates BMI, FI and USA fat percentages and updates corresponding labels
    def calculateAll(self):
        name = self.nameLE.text()
        heigt = self.heightDSB.value()
        weight = self.weightDSB.value()
        self.lPB.setEnabled(False)
        self.savePB.setEnabled(True)
        birthday = self.birthDE.date().toString(format=QtCore.Qt.ISODate) # Covert Birth day to ISO string using QtCores methods
        gender = self.genderCB.currentText() # Set Gender Value according to Combox value
        if gender == 'Mies':
            gender = 1
        else:
            gender = 0
        date = self.wDE.date().toString(format=QtCore.Qt.ISODate) # Covert Weighing day to ISO string using QtCores methods
        age = timetools.datediff_choose_unit(birthday, date, 'year') # Calculate time difference using our home made tools
        
        athlete = kuntoilija.Kuntoilija(name, heigt, weight, age, gender, date)
        bmi = athlete.bmi
        self.painoindexiLabel_2.setText(str(bmi))

    # Saves data to disk    
    def saveData(self):
        pass  

if __name__ == "__main__":
    
    
    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Create the mainwindow (and show it)
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())

   
    # Start the application