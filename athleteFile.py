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
        try:
            with open(file, 'w') as fileToWrite:
                json.dump(data, fileToWrite, indent=2)
            status = (0, 'Tallennus onnistunut', 'All data saved successfully')
        except Exception as error:
            status = (1, 'Tallennus ei onnistunut', str(error))
        return status
    
    def readData(self, file):
        """Reads athlete data from file

        Args:
            file (str): Name of the file

        Returns:
            tupple: Error code, Error message, detailed error message, data
        """
        with open(file, 'r') as fileToRead:
            athlete_data = json.load(fileToRead)
            message = 'OK'
            detailedMessage = 'Data read successfully from disk'
            data = (0, message, detailedMessage, athlete_data)
        return data

    def appendData(self, file, data):
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