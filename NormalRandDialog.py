#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

Dialog for parameter values for the normal and log normal distribution pseudorandom number generation.

"""

from PySide6.QtCore import *
from PySide6.QtWidgets import *
import time

class NormalRandDialog(QDialog):
    def __init__(self, parent=None, lognormal = False):
        """
        Dialog constructor and UI setup.
        :param lognormal: bool if the distribution parameters are for Log Normal.
        """

        super().__init__(parent)
        LogStr = ""
        if lognormal:
            LogStr = "Log "

        self.setWindowTitle(LogStr + "Normal Distribution Generator")

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
        label1 = QLabel("Mu:")
        label2 = QLabel("Sigma:")

        self.num = QSpinBox()
        self.num.setMinimum(1)
        self.num.setMaximum(1000000)
        self.num.setValue(100)
        self.num.setMinimumWidth(100)
        NumLabel = QLabel("Number of random numbers to generate:")

        self.mu = QDoubleSpinBox()
        self.mu.setMinimum(-1000000)
        self.mu.setMaximum(1000000)
        self.mu.setValue(0)
        self.mu.setDecimals(6)
        self.mu.setSingleStep(0.000001)
        self.mu.setMinimumWidth(100)

        self.sigma = QDoubleSpinBox()
        self.sigma.setMinimum(0.000001)
        self.sigma.setMaximum(1000000)
        self.sigma.setValue(1)
        self.sigma.setDecimals(6)
        self.sigma.setSingleStep(0.000001)
        self.sigma.setMinimumWidth(100)

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
        inputs.addWidget(self.mu, 1, 1)
        inputs.addWidget(label2, 2, 0, Qt.AlignRight)
        inputs.addWidget(self.sigma, 2, 1)
        inputs.addWidget(self.clockButton, 0, 2)

        centerlayout = QVBoxLayout()
        centerlayout.addLayout(numLinelayout)
        centerlayout.addLayout(inputs)

        centerlayout.addWidget(buttonBox)
        self.setLayout(centerlayout)
        self.adjustSize()
        self.setFixedSize(self.size())

    def getMu(self):
        """ Gets the mu control value. """
        return self.mu.value()

    def getSigma(self):
        """ Gets the sigma control value. """
        return self.sigma.value()

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
        """ Override of the dialog accept function and checks that the seed is an integer. """
        try:
            if self.Seedtext.text().strip() != "":
                seedVal = int(self.Seedtext.text())
        except:
            QMessageBox.warning(self, "Error", "The seed value must be an integer.", QMessageBox.Ok)
            return False

        super().accept()