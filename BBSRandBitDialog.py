#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

Dialog for parameter values for the Blum-Blum-Shub method for pseudorandom bit generation.

"""
import random

from PySide6.QtCore import *
from PySide6.QtWidgets import *
import time
import SupportFunctions as sf

class BBSRandBitDialog(QDialog):
    def __init__(self, parent=None, mininputwidth=200):
        """
        Dialog constructor and UI setup.
        :param mininputwidth: minimum width of the input text boxes.
        """
        super().__init__(parent)
        self.setWindowTitle("Blum-Blum-Shub Bit Generator")

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
        label1 = QLabel("P:")
        label2 = QLabel("Q:")
        self.text1.setMinimumWidth(mininputwidth)
        self.text2.setMinimumWidth(mininputwidth)

        self.num = QSpinBox()
        self.num.setMinimum(1)
        self.num.setMaximum(1000000)
        self.num.setValue(100)
        self.num.setMinimumWidth(100)
        NumLabel = QLabel("Number of bit sequences to generate:")

        self.bitlength = QSpinBox()
        self.bitlength.setMinimum(1)
        self.bitlength.setMaximum(1000000)
        self.bitlength.setValue(100)
        self.bitlength.setMinimumWidth(100)
        BitLengthLabel = QLabel("Number of bits for each sequences:")

        self.clockButton = QPushButton("Random")
        self.clockButton.clicked.connect(self.SetSeedRandom)

        self.PisPrineButton = QPushButton("Is Prime")
        self.PisPrineButton.clicked.connect(self.PisPrime)

        self.PnextPrineButton = QPushButton("Next Prime")
        self.PnextPrineButton.clicked.connect(self.PnextPrime)

        self.QisPrineButton = QPushButton("Is Prime")
        self.QisPrineButton.clicked.connect(self.QisPrime)

        self.QnextPrineButton = QPushButton("Next Prime")
        self.QnextPrineButton.clicked.connect(self.QnextPrime)

        NumLengthLayout = QGridLayout()
        NumLengthLayout.addWidget(NumLabel, 0, 0, Qt.AlignRight)
        NumLengthLayout.addWidget(self.num, 0, 1)
        NumLengthLayout.addWidget(BitLengthLabel, 1, 0, Qt.AlignRight)
        NumLengthLayout.addWidget(self.bitlength, 1, 1)

        inputs = QGridLayout()
        inputs.addWidget(label1, 0, 0, Qt.AlignRight)
        inputs.addWidget(self.text1, 0, 1)
        inputs.addWidget(self.PisPrineButton, 0, 2)
        inputs.addWidget(self.PnextPrineButton, 0, 3)

        inputs.addWidget(label2, 1, 0, Qt.AlignRight)
        inputs.addWidget(self.text2, 1, 1)
        inputs.addWidget(self.QisPrineButton, 1, 2)
        inputs.addWidget(self.QnextPrineButton, 1, 3)

        inputs.addWidget(seedlabel, 2, 0, Qt.AlignRight)
        inputs.addWidget(self.Seedtext, 2, 1)
        inputs.addWidget(self.clockButton, 2, 2)

        centerlayout = QVBoxLayout()
        centerlayout.addLayout(NumLengthLayout)
        centerlayout.addLayout(inputs)

        centerlayout.addWidget(buttonBox)
        self.setLayout(centerlayout)
        self.adjustSize()
        self.setFixedSize(self.size())

    def getP(self):
        """ Gets P """
        return self.text1.text()

    def getQ(self):
        """ Gets Q """
        return self.text2.text()

    def getSeed(self):
        """ Gets the seed. """
        return self.Seedtext.text()

    def getNumber(self):
        """ Gets the number of bit strings to generate. """
        return self.num.value()

    def getBitLength(self):
        """ Gets the number of bits for each bit string. """
        return self.bitlength.value()

    def SetSeedRandom(self):
        """ Generates a random seed for the generator. """
        try:
            p = int(self.text1.text())
            q = int(self.text2.text())
        except:
            QMessageBox.warning(self, "Input Error", "Both P and Q must be specified and positive integers.", QMessageBox.Ok)
            return
        n = p * q
        posnum = random.randint(2, n - 1)
        while sf.gcd(posnum, n) != 1:
            posnum = random.randint(2, n - 1)
        self.Seedtext.setText(str(posnum))

    def PisPrime(self):
        """ Checks if P is a prime congruent to 3 mod 4. """
        self.isPrimeCheck(self.text1.text(), "P")

    def PnextPrime(self):
        """ Generates the next prime from P that is congruent to 3 mod 4. """
        self.setNextPrime(self.text1)

    def QisPrime(self):
        """ Checks if P is a prime congruent to 3 mod 4. """
        self.isPrimeCheck(self.text2.text(), "Q")

    def QnextPrime(self):
        """ Generates the next prime from Q that is congruent to 3 mod 4. """
        self.setNextPrime(self.text2)

    def isPrimeCheck(self, numstr, PQ = "P"):
        """ Checks if numstr is a prime number congruent to 3 mod 4. """
        try:
            num = int(numstr)
        except:
            QMessageBox.warning(self, "Input Error", "The value must be an integer.", QMessageBox.Ok)
            return
        if num < 2:
            QMessageBox.warning(self, "Input Error", "The value must be at least 2.", QMessageBox.Ok)
            return
        if sf.isPrime(num) and num % 4 == 3:
            QMessageBox.information(self, "Prime Check", PQ + " is probably prime and congruent to 3 mod 4.", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Prime Check", PQ + " is composite or not congruent to 3 mod 4.", QMessageBox.Ok)

    def setNextPrime(self, textbox):
        """ Generates the next prime contained in the textbox that is congruent to 3 mod 4 and sets the box to that value. """
        if textbox.text().strip() == "":
            textbox.setText("2")

        try:
            num = int(textbox.text())
        except:
            QMessageBox.warning(self, "Input Error", "The value must be an integer.", QMessageBox.Ok)
            return
        if num < 2:
            num = 2
        num = sf.nextPrime(num)
        while num % 4 != 3:
            num = sf.nextPrime(num)
        textbox.setText(str(num))

    def accept(self):
        """ Override of the dialog accept function and checks that the two values are primes congruent to 3 mod 4 and that the seed is relatively prime to P*Q. """
        try:
            seedVal = int(self.Seedtext.text())
            p = int(self.text1.text())
            q = int(self.text2.text())

            if p < 2:
                QMessageBox.warning(self, "Input Error", "The value of P must be at least 2.", QMessageBox.Ok)
                return False
            if (not sf.isPrime(p)) or (p % 4 != 3):
                QMessageBox.information(self, "Input Error", "P is composite or not congruent to 3 mod 4.",
                                        QMessageBox.Ok)
                return False

            if q < 2:
                QMessageBox.warning(self, "Input Error", "The value of Q must be at least 2.", QMessageBox.Ok)
                return False
            if (not sf.isPrime(q)) or (q % 4 != 3):
                QMessageBox.information(self, "Input Error", "Q is composite or not congruent to 3 mod 4.",
                                        QMessageBox.Ok)
                return False

            if sf.gcd(seedVal, p*q) != 1:
                QMessageBox.information(self, "Input Error", "The seed must be relatively prime to P*Q.",
                                        QMessageBox.Ok)
                return False
        except:
            QMessageBox.warning(self, "Error", "The P, Q, and seed values must be given and integers.", QMessageBox.Ok)
            return False

        super().accept()