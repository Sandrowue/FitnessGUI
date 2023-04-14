# MAIN WINDOW FOR FITNESS APPLICATION

# Libraries and modules
import sys
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets as QW # UI elements functionality
from PyQt5.uic import loadUi # reads the Ui file
import kuntoilija
import timetools
# Class for the main window
class MainWindow(QW.QMainWindow):
    
    # Constructor for the main window
    def __init__(self):
        super().__init__()
    
        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.heightDSB = self.lengthDoubleSpinBox
        self.heightDSB.valueChanged.connect(self.activateCalculatePB)
        
        self.weightDSB = self.weightDoubleSpinBox
        self.weightDSB.valueChanged.connect(self.activateCalculatePB)

        '''self.nameLE = self.nameLineEdit'''
        self.nameLE = self.findChild(QW.QLineEdit, 'nameLineEdit')
        self.nameLE.textEdited.connect(self.activateCalculatePB)
       
        self.birthDE = self.birthDateEdit
        '''self.birthDE.dateChanged.connect(self.activateCalculatePB)'''

        self.genderCB = self.genderComboBox
        self.genderCB.currentTextChanged.connect(self.activateCalculatePB)
        
        self.wDE = self.weighingDateEdit
        self.wDE.setDate(QtCore.QDate.currentDate()) # Set the weighing date to the current date
        
        self.kaulaSB = self.kaulaSpinBox
        self.kaulaSB.valueChanged.connect(self.activateCalculatePB)

        self.vuotaroSB = self.vyotaroSpinBox
        self.vuotaroSB.valueChanged.connect(self.activateCalculatePB)

        self.lantioSB = self.lantioSpinBox
        self.lantioSB.setEnabled(False)
        self.lantioSB.valueChanged.connect(self.activateCalculatePB)
        
        '''self.lPB = self.laskePushButton'''
        self.lPB = self.findChild(QW.QPushButton, 'laskePushButton')
        self.lPB.clicked.connect(self.calculateAll)
        self.lPB.setEnabled(False)

        '''self.savePB = self.savePushButton'''
        self.savePB = self.findChild(QW.QPushButton, 'savePushButton')
        self.savePB.clicked.connect(self.saveData)
        self.savePB.setEnabled(False)
        
      
    # Define slots ie methods 

    def activateCalculatePB(self):
        self.lPB.setEnabled(True)
        if self.nameLE.text == '':
            self.lPB.setEnabled(False)
        '''if self.birthDE.date() == QtCore.QDate(1980, 1, 1):
            self.lPB.setEnabled(False)'''
        if self.genderCB.currentText() == '':
            self.lPB.setEnabled(False)
        if self.heightDSB.value() == 50:
            self.lPB.setEnabled(False)
        if self.weightDSB.value() == 20:
            self.lPB.setEnabled(False)
        if self.kaulaSB.value() == 10:
            self.lPB.setEnabled(False)
        if self.vuotaroSB.value() == 30:
            self.lPB.setEnabled(False)
        if self.genderCB.currentText() == 'Nainen':
            self.lantioSB.setEnabled(True)
            if self.lantioSB.value() == 30:
                self.lPB.setEnabled(False)
            else:
                self.lPB.setEnabled(False)
            

        
    
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
    app = QW.QApplication(sys.argv)
    
    # Create the mainwindow (and show it)
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())

   
    # Start the application