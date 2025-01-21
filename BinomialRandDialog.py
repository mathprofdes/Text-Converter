#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

Dialog for parameter values for the binomial pseudorandom number generation.

"""

from PySide6.QtCore import *
from PySide6.QtWidgets import *
import time

class BinomailRandDialog(QDialog):
    def __init__(self, parent=None):
        """
        Dialog constructor and UI setup.
        """
        super().__init__(parent)
        self.setWindowTitle("Binomial Distribution Generator")

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
        label1 = QLabel("Trials:")
        label2 = QLabel("Success Probability:")

        self.num = QSpinBox()
        self.num.setMinimum(1)
        self.num.setMaximum(1000000)
        self.num.setValue(100)
        self.num.setMinimumWidth(100)
        NumLabel = QLabel("Number of random numbers to generate:")

        self.trials = QSpinBox()
        self.trials.setMinimum(1)
        self.trials.setMaximum(1000000)
        self.trials.setValue(100)
        self.trials.setMinimumWidth(100)

        self.prob = QDoubleSpinBox()
        self.prob.setMinimum(0)
        self.prob.setMaximum(1)
        self.prob.setValue(0.5)
        self.prob.setDecimals(6)
        self.prob.setSingleStep(0.000001)
        self.prob.setMinimumWidth(100)

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
        inputs.addWidget(self.trials, 1, 1)
        inputs.addWidget(label2, 2, 0, Qt.AlignRight)
        inputs.addWidget(self.prob, 2, 1)
        inputs.addWidget(self.clockButton, 0, 2)

        centerlayout = QVBoxLayout()
        centerlayout.addLayout(numLinelayout)
        centerlayout.addLayout(inputs)

        centerlayout.addWidget(buttonBox)
        self.setLayout(centerlayout)
        self.adjustSize()
        self.setFixedSize(self.size())

    def getTrials(self):
        """ Gets the number of trials. """
        return self.trials.value()

    def getProb(self):
        """ Gets the probability of a success. """
        return self.prob.value()

    def getSeed(self):
        """ Gets the value of the seed. """
        return self.Seedtext.text()

    def getNumber(self):
        """ Gets the number of values to generate. """
        return self.num.value()

    def SetSeedToClock(self):
        """ Sets the seed value to the current CPU clock time. """
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