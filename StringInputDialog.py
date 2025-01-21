#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

General dialog for the user to input a single string.

"""

from PySide6.QtCore import *
from PySide6.QtWidgets import *


class StringInputDialog(QDialog):
    def __init__(self, parent=None, title="Input a String", message="", itemMessage="", mininputwidth=200):
        """
        Dialog constructor and UI setup.
        :param title: Dialog box title.
        :param message: Message to the user.
        :param itemMessage: Label before the input control.
        :param mininputwidth: Width of the input text box.
        """

        super().__init__(parent)
        self.setWindowTitle(title)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        buttonBox.button(QDialogButtonBox.Ok).setAutoDefault(True)
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
        buttonBox.button(QDialogButtonBox.Cancel).setAutoDefault(False)
        buttonBox.button(QDialogButtonBox.Cancel).setDefault(False)

        messagelabel = QLabel(message)

        self.text1 = QLineEdit()
        label1 = QLabel(itemMessage)
        self.text1.setMinimumWidth(mininputwidth)

        inputs = QGridLayout()
        inputs.addWidget(label1, 0, 0, Qt.AlignRight)
        inputs.addWidget(self.text1, 0, 1)

        centerlayout = QVBoxLayout()
        centerlayout.addWidget(messagelabel)
        centerlayout.addLayout(inputs)

        centerlayout.addWidget(buttonBox)
        self.setLayout(centerlayout)
        self.adjustSize()
        self.setFixedSize(self.size())

    def getText(self):
        """ Gets the text from the text input box. """
        return self.text1.text()
