#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

General dialog for the user to input a single integer.

"""

from PySide6.QtCore import *
from PySide6.QtWidgets import *


class OneNumberInputDialog(QDialog):
    def __init__(self, parent=None, title="Input a Number", message="", item1Message="",
                 spin1low=0, spin1high=100, spin1val=10, spinwidth=50):
        """
        Dialog constructor and UI setup.
        :param title: Dialog box title.
        :param message: Message to the user.
        :param item1Message: Label before the input control.
        :param spin1low: Lower bound for the spinner control.
        :param spin1high: Upper bound for the spinner control.
        :param spin1val: Default value for the spinner control.
        :param spinwidth: Width of the spinner control.
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

        self.num1 = QSpinBox()
        self.num1.setMinimum(spin1low)
        self.num1.setMaximum(spin1high)
        self.num1.setValue(spin1val)
        self.num1.setMinimumWidth(spinwidth)
        label1 = QLabel(item1Message)

        inputs = QGridLayout()
        inputs.addWidget(label1, 0, 0, Qt.AlignRight)
        inputs.addWidget(self.num1, 0, 1)

        inputArea = QHBoxLayout()
        inputArea.addLayout(inputs)
        inputArea.addStretch(0)

        centerlayout = QVBoxLayout()
        centerlayout.addWidget(messagelabel)
        centerlayout.addLayout(inputArea)

        centerlayout.addWidget(buttonBox)
        self.setLayout(centerlayout)
        self.adjustSize()
        self.setFixedSize(self.size())

    def getVal(self):
        """ Gets the spinner control value. """
        return self.num1.value()
