#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

General dialog for the user to input a two integers.

"""

from PySide6.QtCore import *
from PySide6.QtWidgets import *


class TwoNumberInputDialog(QDialog):
    def __init__(self, parent=None, title="Input Two Numbers", message="", item1Message="", item2Message="",
                 spin1low=0, spin1high=100, spin1val=10, spin2low=0, spin2high=100,
                 spin2val=10, spinwidth=50):
        """
        Dialog constructor and UI setup.
        :param title: Dialog box title.
        :param message: Message to the user.
        :param item1Message: Label before the input control #1.
        :param item2Message: Label before the input control #2.
        :param spin1low: Lower bound for the spinner control #1.
        :param spin1high: Upper bound for the spinner control #1.
        :param spin1val: Default value for the spinner control #1.
        :param spin2low: Lower bound for the spinner control #2.
        :param spin2high: Upper bound for the spinner control #2.
        :param spin2val: Default value for the spinner control #2.
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

        self.num2 = QSpinBox()
        self.num2.setMinimum(spin2low)
        self.num2.setMaximum(spin2high)
        self.num2.setValue(spin2val)
        self.num2.setMinimumWidth(spinwidth)
        label2 = QLabel(item2Message)

        inputs = QGridLayout()
        inputs.addWidget(label1, 0, 0, Qt.AlignRight)
        inputs.addWidget(self.num1, 0, 1)
        inputs.addWidget(label2, 1, 0, Qt.AlignRight)
        inputs.addWidget(self.num2, 1, 1)

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

    def getVal1(self):
        """ Gets the spinner control #1 value. """
        return self.num1.value()

    def getVal2(self):
        """ Gets the spinner control #2 value. """
        return self.num2.value()
