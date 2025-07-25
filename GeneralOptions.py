"""
Options for the Text Converter Font

self.Font - QFont font for the editor text.
"""

from PySide6.QtGui import QFont, QColor


class GeneralOptions:
    def __init__(self):
        self.Font = QFont('Courier New', 12)
        self.highlightColor = QColor(235, 235, 255)
        self.theme = 'Fusion'

    def toList(self) -> []:
        """
        Creates a list of all data in the class for saving to a file.

        Returns: List of class data.
        """
        retlist = []
        retlist.append(self.Font.toString())
        retlist.append([self.highlightColor.red(), self.highlightColor.green(), self.highlightColor.blue()])
        retlist.append(self.theme)
        return retlist

    def fromList(self, datalist: []) -> bool:
        """
        Loads the data from the list into the class variables.

        Parameters:
            datalist - list of class data as was returned from toList.
        Returns: True if all data was loaded successfully and False otherwise.
        """
        try:
            self.Font.fromString(datalist[0])
            collist = datalist[1]
            self.highlightColor = QColor(collist[0], collist[1], collist[2])
            self.theme = datalist[2]
            return True
        except:
            return False
