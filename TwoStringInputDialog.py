#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

General dialog for the user to input two strings.

"""

from PySide6.QtCore import *
from PySide6.QtWidgets import *


class TwoStringInputDialog(QDialog):
    def __init__(self, parent=None, title="Input Two Strings", message="", item1Message="", item2Message="", mininputwidth=200):
        """
        Dialog constructor and UI setup.
        :param title: Dialog box title.
        :param message: Message to the user.
        :param item1Message: Label before the input control #1.
        :param item2Message: Label before the input control #2.
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
        self.text2 = QLineEdit()
        label1 = QLabel(item1Message)
        label2 = QLabel(item2Message)
        self.text1.setMinimumWidth(mininputwidth)

        inputs = QGridLayout()
        inputs.addWidget(label1, 0, 0, Qt.AlignRight)
        inputs.addWidget(self.text1, 0, 1)
        inputs.addWidget(label2, 1, 0, Qt.AlignRight)
        inputs.addWidget(self.text2, 1, 1)

        centerlayout = QVBoxLayout()
        centerlayout.addWidget(messagelabel)
        centerlayout.addLayout(inputs)

        centerlayout.addWidget(buttonBox)
        self.setLayout(centerlayout)
        self.adjustSize()
        self.setFixedSize(self.size())

    def getText1(self):
        """ Gets the text from the text input box #1. """
        return self.text1.text()

    def getText2(self):
        """ Gets the text from the text input box #2. """
        return self.text2.text()
