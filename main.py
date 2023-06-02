# MAIN WINDOW FOR FITNESS APPLICATION

# Libraries and modules
import sys
from PyQt5 import QtCore # Core functionality of Qt
from PyQt5 import QtWidgets as QW # UI elements functionality
from PyQt5.uic import loadUi # reads the Ui file
import kuntoilija
import athleteFile
import timetools
import ohjeDialog
import Kuntoilija_mainwindow
# Class for the main window
class MainWindow(QW.QMainWindow):
    
    # Constructor for the main window
    def __init__(self):
        super().__init__()
    
        # Load the UI file
        loadUi('main.ui', self)

        # Define UI Controls ie buttons and input fields
        self.heightVS = self.lengthVerticalSlider
        self.heightVS.valueChanged.connect(self.activateCalculatePB)
        
        self.weightD = self.weightDial
        self.weightD.valueChanged.connect(self.activateCalculatePB)

        '''self.nameLE = self.nameLineEdit'''
        self.nameLE = self.findChild(QW.QLineEdit, 'nameLineEdit')
        self.nameLE.textEdited.connect(self.activateCalculatePB)
       
        self.birthDE = self.birthDateEdit
        '''self.birthDE.dateChanged.connect(self.activateCalculatePB)'''

        self.genderCB = self.genderComboBox
        self.genderCB.currentTextChanged.connect(self.activateCalculatePB)
        
        self.wDE = self.weighingDateEdit
        self.wDE.setDate(QtCore.QDate.currentDate()) # Set the weighing date to the current date
        
        self.kaulaHS = self.kaulaHorizontalSlider
        self.kaulaHS.valueChanged.connect(self.activateCalculatePB)

        self.vuotaroHS = self.vyutaroHorizontalSlider
        self.vuotaroHS.valueChanged.connect(self.activateCalculatePB)

        self.lantioHS = self.lantioHorizontalSlider
        self.lantioHS.setEnabled(False)
        self.lantioHS.valueChanged.connect(self.activateCalculatePB)
        
        self.dimensionBox = self.frame

        #Create a status bar for showing informational messages
        self.statusBar = QW.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.show()

        '''self.lPB = self.laskePushButton'''
        self.lPB = self.findChild(QW.QPushButton, 'laskePushButton')
        self.lPB.clicked.connect(self.calculateAll)
        self.lPB.setEnabled(False)

        self.testPB = self.testPushButton
        self.testPB.clicked.connect(self.insertTestValues)
      
        '''self.savePB = self.savePushButton'''
        self.savePB = self.findChild(QW.QPushButton, 'savePushButton')
        self.savePB.clicked.connect(self.saveData)
        self.savePB.setEnabled(False)
        
        # Read data from file and save it to a list
        self.dataList = []
        jsonFile = athleteFile.ProcessJsonFile()
        try:
            data = jsonFile.readData('athleteData.json')
            self.dataList = data[3]
        except Exception as e:
            data = (1, 'Error', str(e), self.dataList)
           
        # Menu Actions
        self.actionPalauta_oletukset.triggered.connect(self.restoreDefaults)
        self.actionAvaa_Ohjeet.triggered.connect(self.openHelpDialog)




    # Define slots ie methods 

    # Create a alerting method
    def alert(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Critical)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    def warn(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Warning)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    def inform(self, windowTitle, message, detailedMessage):
        msgBox = QW.QMessageBox()
        msgBox.setIcon(QW.QMessageBox.Information)
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    def showMessageBox(self, windowTitle, message, detailedMessage, icon='Information'):
        """Creates a message box for various types of messages

        Args:
            windowTitle (str): Header for the message window
            message (str): Message to be shown
            detailedMessage (str): A message that con be shown by pressing details button
            icon (str, optional): Defaults to 'Information'. Allowed values: 
            NoIcon, Information, Question, Warning and Critical
        """
        iconTypes = {'Information': QW.QMessageBox.Information, 'NoIcon': QW.QMessageBox.NoIcon, 'Question': QW.QMessageBox.Question, 
         'Warning': QW.QMessageBox.Warning, 'Critical': QW.QMessageBox.critical}
        msgBox = QW.QMessageBox()
        msgBox.setIcon(iconTypes[icon])
        msgBox.setWindowTitle(windowTitle)
        msgBox.setText(message)
        msgBox.setDetailedText(detailedMessage)
        msgBox.exec()

    def activateCalculatePB(self):
        self.lPB.setEnabled(True)
        if self.nameLE.text == '':
            self.lPB.setEnabled(False)
        '''if self.birthDE.date() == QtCore.QDate(1980, 1, 1):
            self.lPB.setEnabled(False)'''
        if self.genderCB.currentText() == '':
            self.lPB.setEnabled(False)
        if self.heightVS.value() == 50:
            self.lPB.setEnabled(False)
        if self.weightD.value() == 20:
            self.lPB.setEnabled(False)
        if self.kaulaHS.value() == 10:
            self.lPB.setEnabled(False)
        if self.vuotaroHS.value() == 30:
            self.lPB.setEnabled(False)
        if self.genderCB.currentText() == 'Nainen':
            self.lantioLabel.show()
            self.lantioHS.setEnabled(True)
            self.lantioHS.show()
            self.dimensionBox.setStyleSheet("background-image: url(NaisSlice_original.png)")
            if self.lantioHS.value() == 30:
                self.lPB.setEnabled(False)
        else:
            self.lPB.setEnabled(True)
            self.lantioHS.hide()
            self.lantioLabel.hide()
            self.dimensionBox.setStyleSheet("background-image: url(MiesSlice.png)")
            

        
    
    # Calculates BMI, FI and USA fat percentages and updates corresponding labels
    def insertTestValues(self):
        self.nameLE.setText('Teppo Testi')
        testbirthDate = QtCore.QDate(1980, 1, 1)
        self.birthDE.setDate(testbirthDate)
        self.genderCB.setCurrentText('Mies')
        self.heightVS.setValue(178)
        self.weightD.setValue(70)
        self.kaulaHS.setValue(30)
        self.vuotaroHS.setValue(90)
        

    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightVS.value()
        weight = self.weightD.value()
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
        kaula = self.kaulaHS.value()
        if kaula < 15:
            #self.alert('Tarkista kaulan ympäryys', 'Kaulan ymärys liian pieni', 'Kaulan koko pitää olla enemmän kuin 15cm')
            self.showMessageBox('Tarkista kaulan ympärys', 'Kaulan ympärys liian pieni', 'Kaulan koko pitää alla enemmän kuin 15cm', 'Warning')
        vyötärö = self.vuotaroHS.value()
        lantio = self.lantioHS.value()

        athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, kaula, vyötärö, lantio, date)
        
        '''if age > 18:
            athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, date)
        else:
            athlete = kuntoilija.JunioriKuntoilija(name, height, weight, age, gender)'''
        bmi = athlete.bmi
        self.painoindexiLabel_2.setText(str(bmi))
        
        finFatPercentage = athlete.fi_rasva
        usaFatPercentage = athlete.usa_rasva
        '''if gender == 1:
            usaFatPercentage = athlete.usa_rasvaprosentti_mies(height, vyötärö, kaula)
        else:
            usaFatPercentage = athlete.usa_rasvaprosentti_nainen(height, vyötärö, lantio, kaula)'''
        
        self.rasvaprosentti_FI_label_2.setText(str(finFatPercentage))
        self.rasvaprosentti_USA_label_2.setText(str(usaFatPercentage))

        self.dataRow = self.constructData(athlete)
        print(self.dataRow)

    def constructData(self, athlete,):
        athlete_data_row = {'nimi': athlete.nimi, 'pituus': athlete.pituus, 'paino': athlete.paino, 'ika': athlete.ika, 'sukupuoli': athlete.sukupuoli,
                    'pvm': athlete.punnitus_paiva, 'bmi': athlete.bmi, 'rasvaprosenttiFi': athlete.fi_rasva, 'rasvaprosenttiUs': athlete.usa_rasva}
        return athlete_data_row
        
    # Saves data to disk    
    def saveData(self):
        self.dataList.append(self.dataRow)  
        jsonFile2 = athleteFile.ProcessJsonFile()
        status = jsonFile2.saveData('athleteData.json', self.dataList)
        self.statusBar.showMessage(status[1], 4000) # Show message about status of saving on statusbar
        if status[0] != 0:
            self.alert(status[1], status[2])
        else:
            self.restoreDefaults

    def restoreDefaults(self):
        self.nameLE.clear()
        zeroDate = QtCore.QDate(1980, 1, 1)
        self.birthDE.setDate(zeroDate)
        self.heightVS.setValue(50)
        self.weightD.setValue(20)
        self.kaulaHS.setValue(10)
        self.vuotaroHS.setValue(30)
        self.lantioHS.setValue(30)
        self.savePB.setEnabled(False)

    def openHelpDialog(self):
        openHelp = ohjeDialog.OpenHelp()
        openHelp.exec()

if __name__ == "__main__":
    
    
    # Create the application
    app = QW.QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Create the mainwindow (and show it)
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())

   
    # Start the application