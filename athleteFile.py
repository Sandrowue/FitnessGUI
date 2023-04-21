# ROUTINES TO CREATE, WRITE AND READ ATHLETE DATA FILE

import json

'''athlete_data_row = {'nimi': athlete.nimi, 'pituus': athlete.pituus, 'paino': athlete.paino, 'ika': athlete.ika, 'sukupuoli': athlete.sukupuoli,
                    'pvm': athlete.punnitus_paiva}'''

class ProcessJsonFile():
    def __init__(self):
        pass
    
   

    def saveData(self, file, data):
        """Saves all athlete data to disk

        Args:
            file (str): Name of the file
            data (list): List of dictionaries

        Returns:
            tuple: Error code, Error message, detailed error message
        """
        status = (0, 'Tallennus onnistunut', 'All data saved successfully')
        return status
    
    def readData(self, file):
        """Reads athlete data from file

        Args:
            file (str): Name of the file

        Returns:
            tupple: Error code, Error message, detailed error message, data
        """
        data = (0, message, detailedMessage, readInfo)
        return data

    def appendDate(self, file, data):
        """Adds a new json object to the file

        Args:
            file (str): Name of the file
            data (dict): python dictionary containing data

        Returns:
            tuple: Error code, Error message, detailed error message
        """
        status = (0, 'Tallennus onnistunut', 'Data saved successfully')
        return status




if __name__ == "__main__":
    pass