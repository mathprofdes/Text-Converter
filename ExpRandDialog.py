#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

Dialog for parameter values for the exponential pseudorandom number generation.

"""

from PySide6.QtCore import *
from PySide6.QtWidgets import *
import time

class ExpRandDialog(QDialog):
    def __init__(self, parent=None):
        """
        Dialog constructor and UI setup.
        """
        super().__init__(parent)
        self.setWindowTitle("Exponential Distribution Generator")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        buttonBox.button(QDialogButtonBox.Ok).setAutoDefault(True)
        buttonBox.button(QDialogButtonBox.Ok).setDefault(True)
        buttonBox.button(QDialogButtonBox.Cancel).setAutoDefault(False)
        buttonBox.button(QDialogButtonBox.Cancel).setDefault(False)

        self.Seedtext = QLineEdit()
        seedlabel = QLabel("Seed:")
        label1 = QLabel("Lambda:")

        self.num = QSpinBox()
        self.num.setMinimum(1)
        self.num.setMaximum(1000000)
        self.num.setValue(100)
        self.num.setMinimumWidth(100)
        NumLabel = QLabel("Number of random numbers to generate:")

        self.lamb = QDoubleSpinBox()
        self.lamb.setMinimum(-1000000)
        self.lamb.setMaximum(1000000)
        self.lamb.setValue(1)
        self.lamb.setDecimals(6)
        self.lamb.setSingleStep(0.000001)
        self.lamb.setMinimumWidth(100)

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
        inputs.addWidget(self.lamb, 1, 1)
        inputs.addWidget(self.clockButton, 0, 2)

        centerlayout = QVBoxLayout()
        centerlayout.addLayout(numLinelayout)
        centerlayout.addLayout(inputs)

        centerlayout.addWidget(buttonBox)
        self.setLayout(centerlayout)
        self.adjustSize()
        self.setFixedSize(self.size())

    def getLambda(self):
        """ Gets the lambda control value. """
        return self.lamb.value()

    def getSeed(self):
        """ Gets the seed control value. """
        return self.Seedtext.text()

    def getNumber(self):
        """ Gets the number control value. """
        return self.num.value()

    def SetSeedToClock(self):
        """ Sets the seed to the current CPU clock value. . """
        self.Seedtext.setText(str(int(time.time()*1000000)))

    def accept(self):
        """ Override of the dialog accept function and checks that the seed is an integer and that lambda is not 0. """
        try:
            if self.Seedtext.text().strip() != "":
                seedVal = int(self.Seedtext.text())
        except:
            QMessageBox.warning(self, "Error", "The seed value must be an integer.", QMessageBox.Ok)
            return False

        if self.lamb.value() == 0:
            QMessageBox.warning(self, "Error", "Lambda cannot be 0.", QMessageBox.Ok)
            return False

        super().accept()