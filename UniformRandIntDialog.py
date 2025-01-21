#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

Dialog for parameter values for the uniform distribution pseudorandom number generation for both integers and floats.

"""

from PySide6.QtCore import *
from PySide6.QtWidgets import *
import time

class UniformRandIntDialog(QDialog):
    def __init__(self, parent=None, title = "Uniform Random Integer Generator", mininputwidth=200, intType = True):
        """
        Dialog constructor and UI setup.
        :param title: Title of the dialog box.
        :param mininputwidth: Width of the input control.
        :param intType: bool if the data type is integer and false if it is float.
        """

        super().__init__(parent)
        self.setWindowTitle(title)
        self.intType = intType

        if self.intType:
            self.typestr = "an integer"
        else:
            self.typestr = "a float"

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        buttonBox.button(QDialogButtonBox.Ok).setAutoDefault(True)
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
        buttonBox.button(QDialogButtonBox.Cancel).setAutoDefault(False)
        buttonBox.button(QDialogButtonBox.Cancel).setDefault(False)

        self.Seedtext = QLineEdit()
        self.text1 = QLineEdit()
        self.text2 = QLineEdit()
        seedlabel = QLabel("Seed:")
        label1 = QLabel("Lower Bound:")
        label2 = QLabel("Upper Bound:")
        self.text1.setMinimumWidth(mininputwidth)
        self.text2.setMinimumWidth(mininputwidth)

        self.num = QSpinBox()
        self.num.setMinimum(1)
        self.num.setMaximum(1000000)
        self.num.setValue(100)
        self.num.setMinimumWidth(100)
        NumLabel = QLabel("Number of random numbers to generate:")

        self.clockButton = QPushButton("Use Clock")
        self.clockButton.clicked.connect(self.SetSeedToClock)

        numLinelayout = QHBoxLayout()
        numLinelayout.addWidget(NumLabel)
        numLinelayout.addWidget(self.num)
        numLinelayout.addStretch(0)

        inputs = QGridLayout()
        inputs.addWidget(seedlabel, 0, 0, Qt.AlignRight)
        inputs.addWidget(self.Seedtext, 0, 1)
        inputs.addWidget(label1, 1, 0, Qt.AlignRight)
        inputs.addWidget(self.text1, 1, 1)
        inputs.addWidget(label2, 2, 0, Qt.AlignRight)
        inputs.addWidget(self.text2, 2, 1)
        inputs.addWidget(self.clockButton, 0, 2)

        centerlayout = QVBoxLayout()
        centerlayout.addLayout(numLinelayout)
        centerlayout.addLayout(inputs)

        centerlayout.addWidget(buttonBox)
        self.setLayout(centerlayout)
        self.adjustSize()
        self.setFixedSize(self.size())

    def getLowerBound(self):
        """ Gets the lower bound for the range. """
        return self.text1.text()

    def getUpperBound(self):
        """ Gets the upper bound for the range. """
        return self.text2.text()

    def getSeed(self):
        """ Gets the seed for the random number generator. """
        return self.Seedtext.text()

    def getNumber(self):
        """ Gets the number of values to generate. """
        return self.num.value()

    def SetSeedToClock(self):
        """ Sets the seed to the current time on the CPU clock. """
        self.Seedtext.setText(str(int(time.time()*1000000)))

    def accept(self):
        """ Override of the dialog accept function and checks that the seed is an integer and that the lower and upper bounds are the correct data type. """
        try:
            if self.Seedtext.text().strip() != "":
                seedVal = int(self.Seedtext.text())
        except:
            QMessageBox.warning(self, "Error", "The seed value must be an integer.", QMessageBox.Ok)
            return False

        try:
            if self.text1.text().strip() != "":
                if self.intType:
                    val = int(self.text1.text())
                else:
                    val = float(self.text1.text())
        except:
            QMessageBox.warning(self, "Error", "The lower bound value must be "+ self.typestr + ".", QMessageBox.Ok)
            return False

        try:
            if self.text2.text().strip() != "":
                if self.intType:
                    val = int(self.text2.text())
                else:
                    val = float(self.text2.text())
        except:
            QMessageBox.warning(self, "Error", "The upper bound value must be " + self.typestr + ".", QMessageBox.Ok)
            return False

        super().accept()