#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 7/20/2024

@author: Don Spickler

"""

import pickle
import platform
import sys
import os
import copy
import math
import webbrowser

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtPrintSupport import *

from GeneralOptions import GeneralOptions
from InputPane import *
from CSS_Class import appcss

# For the Mac OS
os.environ['QT_MAC_WANTS_LAYER'] = '1'


class TextConverter(QMainWindow):

    def __init__(self, title="Text Converter"):
        super().__init__()
        # About information for the app.
        self.authors = "Don Spickler"
        self.version = "1.2.1"
        self.program_title = "Text Converter"
        self.copyright = "2025"

        self.licence = "\nThis software is distributed under the GNU General Public License version 3.\n\n" + \
                       "This program is free software: you can redistribute it and/or modify it under the terms of the GNU " + \
                       "General Public License as published by the Free Software Foundation, either version 3 of the License, " + \
                       "or (at your option) any later version. This program is distributed in the hope that it will be useful, " + \
                       "but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A " + \
                       "PARTICULAR PURPOSE. See the GNU General Public License for more details http://www.gnu.org/licenses/."

        self.setWindowTitle(self.program_title)
        self.initializeUI()
        self.setMinimumSize(QSize(700, 300))
        self.setGeometry(100, 100, 700, 500)
        icon = QIcon(self.resource_path("icons/gnome-run.png"))
        self.setWindowIcon(icon)
        self.show()

    def initializeUI(self):
        self.inputpane = InputPane(False, "", False, False, True, True)
        self.setCentralWidget(self.inputpane)

        # Add Icons to existing menu options
        self.inputpane.file_new_act.setIcon(QIcon(self.resource_path("icons/FileNew.png")))
        self.inputpane.file_open_act.setIcon(QIcon(self.resource_path("icons/FileOpen.png")))
        self.inputpane.file_saveas_act.setIcon(QIcon(self.resource_path("icons/FileSave.png")))
        self.inputpane.file_print_act.setIcon(QIcon(self.resource_path("icons/print.png")))
        self.inputpane.file_PrintPreview_act.setIcon(QIcon(self.resource_path("icons/preview.png")))
        self.inputpane.edit_cut_act.setIcon(QIcon(self.resource_path("icons/Delete.png")))
        self.inputpane.edit_copy_act.setIcon(QIcon(self.resource_path("icons/copy.png")))
        self.inputpane.edit_paste_act.setIcon(QIcon(self.resource_path("icons/paste.png")))
        self.inputpane.edit_undo_act.setIcon(QIcon(self.resource_path("icons/Undo.png")))
        self.inputpane.edit_redo_act.setIcon(QIcon(self.resource_path("icons/Redo.png")))

        self.inputpane.file_menu.addSeparator()

        self.exit_act = QAction("Exit", self)
        self.exit_act.triggered.connect(self.onExit)
        self.inputpane.file_menu.addAction(self.exit_act)

        # Additional Menu Options
        options_menu = self.inputpane.menu.addMenu("Options")
        self.ResetFont_act = QAction("Reset Font", self)
        self.ResetFont_act.triggered.connect(self.onResetFont)

        self.FontBold_act = QAction("Toggle Bold", self)
        self.FontBold_act.triggered.connect(self.onFontBold)

        self.FontItalic_act = QAction("Toggle Italic", self)
        self.FontItalic_act.triggered.connect(self.onFontItalic)

        self.FontSize_act = QAction("Font Size...", self)
        self.FontSize_act.triggered.connect(self.onFontSize)

        self.SelectFont_act = QAction("Select Font...", self)
        self.SelectFont_act.triggered.connect(self.onSelectFont)

        options_menu.addAction(self.FontBold_act)
        options_menu.addAction(self.FontItalic_act)
        options_menu.addAction(self.FontSize_act)
        options_menu.addSeparator()
        options_menu.addAction(self.SelectFont_act)
        options_menu.addSeparator()
        options_menu.addAction(self.ResetFont_act)

        ###  Help Menu
        help_menu = self.inputpane.menu.addMenu("Help")

        self.help_act = QAction("Help...", self)
        self.help_act.setIcon(QIcon(self.resource_path("icons/Help2.png")))
        self.help_act.triggered.connect(self.onHelp)
        help_menu.addAction(self.help_act)

        self.help_about_act = QAction("About...", self)
        self.help_about_act.setIcon(QIcon(self.resource_path("icons/About.png")))
        self.help_about_act.triggered.connect(self.aboutDialog)
        help_menu.addAction(self.help_about_act)

        try:
            with open('TextConverterOptions.opt', 'rb') as f:
                filecontents = pickle.load(f)
                optList = GeneralOptions()
                optList.fromList(filecontents)
                doc = self.inputpane.editor.document()
                doc.setDefaultFont(optList.Font)
        except:
            pass

    def onExit(self):
        self.close()

    def onResetFont(self):
        doc = self.inputpane.editor.document()
        font = doc.defaultFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setItalic(False)
        font.setPointSize(12)
        doc.setDefaultFont(font)
        self.saveOptions()

    def onFontBold(self):
        doc = self.inputpane.editor.document()
        font = doc.defaultFont()
        font.setBold(not font.bold())
        doc.setDefaultFont(font)
        self.saveOptions()

    def onFontItalic(self):
        doc = self.inputpane.editor.document()
        font = doc.defaultFont()
        font.setItalic(not font.italic())
        doc.setDefaultFont(font)
        self.saveOptions()

    def onFontSize(self):
        doc = self.inputpane.editor.document()
        font = doc.defaultFont()
        oldsize = font.pointSize()

        dialog = OneNumberInputDialog(self, "Font Size",
                                      "Input the editor font size.", "Size:",
                                      5, 72, oldsize,  50)
        if dialog.exec():
            newsize = dialog.getVal()
            doc = self.inputpane.editor.document()
            font = doc.defaultFont()
            font.setPointSize(newsize)
            doc.setDefaultFont(font)
            self.saveOptions()

    def onSelectFont(self):
        doc = self.inputpane.editor.document()
        font = doc.defaultFont()
        fontdialog = QFontDialog()
        fontdialog.setCurrentFont(font)
        if fontdialog.exec():
            font = fontdialog.selectedFont()
            doc.setDefaultFont(font)
            self.saveOptions()

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    # Display information about program dialog box
    def aboutDialog(self):
        QMessageBox.about(self, self.program_title + "  Version " + self.version,
                          self.authors + "\nVersion " + self.version +
                          "\nCopyright " + self.copyright +
                          "\nDeveloped in Python using the PySide6 GUI toolset.\n" +
                          self.licence
                          )

    def saveOptions(self):
        opts = GeneralOptions()
        doc = self.inputpane.editor.document()
        font = doc.defaultFont()
        opts.Font = font
        optlist = opts.toList()
        with open('TextConverterOptions.opt', 'wb') as f:
            try:
                pickle.dump(optlist, f)
            except:
                QMessageBox.warning(self, "File Not Saved", "The options file could not be saved.",
                                    QMessageBox.Ok)

    # Open the help system in the systems default browser.
    def onHelp(self):
        self.url_home_string = "file://" + self.resource_path("Help/index.html")
        webbrowser.open(self.url_home_string)

    def closeEvent(self, event):
        pass
        # count = 0
        # for i in range(len(self.WindowList)):
        #     if self.WindowList[i].isVisible():
        #         count += 1
        #
        # if count > 0:
        #     close = QMessageBox.warning(self, "Exit Program",
        #                                      "All open windows will be closed and current states lost.  " +
        #                                      "Are you sure want to exit the program?",
        #                                      QMessageBox.Yes | QMessageBox.No)
        #     if close == QMessageBox.Yes:
        #         event.accept()
        #         for i in range(len(self.WindowList)):
        #             self.WindowList[i].close()
        #     else:
        #         event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextConverter(app)
    progcss = appcss()
    app.setStyleSheet(progcss.getCSS())

    # Load file parameter if one is given.
    # if len(sys.argv) > 1:
    #     window.openFile(sys.argv[1])

    # plat = platform.system()
    # styles = QStyleFactory.keys()
    #
    # if (plat == "Windows") and ("Windows" in styles):
    #     app.setStyle('Windows')
    # if (plat == "Darwin") and ("Windows" in styles):
    #     app.setStyle('Windows')

    # sys.exit(app.exec_())
    sys.exit(app.exec())
