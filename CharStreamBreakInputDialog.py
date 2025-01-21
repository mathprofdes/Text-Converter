#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

Dialog for parameter values for the character stream breaking function.

"""

from PySide6.QtCore import *
from PySide6.QtWidgets import *

class CharStreamBreakInputDialog(QDialog):
    def __init__(self, parent=None, title="Break Character Stream",
                 message="Break character stream into blocks of N characters.",
                 labelMessage="Block Size (N):", showPresWords=True):
        """
        Dialog constructor and UI setup.
        :param title: Title of the dialog box.
        :param message: Message of what to inout.
        :param labelMessage: Short message label before the input control.
        :param showPresWords: bool to show a preserve words check box option.
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

        self.sizeN = QSpinBox()
        self.sizeN.setMinimum(1)
        self.sizeN.setMaximum(1000)
        self.sizeN.setValue(80)
        self.sizeN.setMinimumWidth(100)
        label1 = QLabel(labelMessage)
        self.preserveWords = QCheckBox("Preserve Words")

        NinputLine = QHBoxLayout()
        NinputLine.addWidget(label1)
        NinputLine.addWidget(self.sizeN)
        NinputLine.addStretch()

        centerlayout = QVBoxLayout()
        centerlayout.addWidget(messagelabel)
        centerlayout.addLayout(NinputLine)
        if showPresWords:
            centerlayout.addWidget(self.preserveWords)

        centerlayout.addWidget(buttonBox)
        self.setLayout(centerlayout)
        self.adjustSize()
        self.setFixedSize(self.size())

    def getNum(self):
        """ Gets the number control value. """
        return self.sizeN.value()

    def getPreserveWords(self):
        """ Gets the checked state of the preserve words checkbox. """
        return self.preserveWords.isChecked()

