#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 6/15/2025

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

    def __init__(self, parent = None, title="Text Editor & Converter", filetoload = ''):
        super().__init__()
        # About information for the app.
        self.authors = "Don Spickler"
        self.version = "1.3.1"
        self.program_title = "Text Editor & Converter"
        self.copyright = "2025"

        self.licence = "\nThis software is distributed under the GNU General Public License version 3.\n\n" + \
                       "This program is free software: you can redistribute it and/or modify it under the terms of the GNU " + \
                       "General Public License as published by the Free Software Foundation, either version 3 of the License, " + \
                       "or (at your option) any later version. This program is distributed in the hope that it will be useful, " + \
                       "but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A " + \
                       "PARTICULAR PURPOSE. See the GNU General Public License for more details http://www.gnu.org/licenses/."

        self.setWindowTitle(self.program_title)
        self.programList = []
        self.Parent = parent

        self.currentTheme = ''
        self.Platform = platform.system()
        styles = QStyleFactory.keys()
        if "Fusion" in styles:
            app.setStyle('Fusion')
            self.currentTheme = 'Fusion'
        else:
            self.currentTheme = styles[0]

        self.initializeUI(filetoload)
        self.setMinimumSize(QSize(700, 300))
        self.setGeometry(100, 100, 700, 500)
        icon = QIcon(self.resource_path("ProgramIcon.png"))
        self.setWindowIcon(icon)
        self.show()

    def initializeUI(self, filetoload = ''):
        self.inputpane = InputPane(False, "", False, False, True, True)
        self.setCentralWidget(self.inputpane)

        self.inputpane.file_menu.addSeparator()
        self.newEditorWindow_act = QAction("Open a New Editor Window...", self)
        self.newEditorWindow_act.triggered.connect(self.onNewWindow)
        self.newEditorWindow_act.setStatusTip('Open a new editor window.')
        self.inputpane.file_menu.addAction(self.newEditorWindow_act)

        self.inputpane.file_menu.addSeparator()
        self.exit_act = QAction("Exit", self)
        self.exit_act.triggered.connect(self.onExit)
        self.exit_act.setStatusTip('Quit the program.')
        self.inputpane.file_menu.addAction(self.exit_act)

        # Additional Menu Options
        options_menu = self.inputpane.menu.addMenu("Options")
        self.ResetFont_act = QAction("Reset Font", self)
        self.ResetFont_act.setStatusTip('Reset the font to the default.')
        self.ResetFont_act.triggered.connect(self.onResetFont)

        self.FontBold_act = QAction("Toggle Bold", self)
        self.FontBold_act.triggered.connect(self.onFontBold)
        self.FontBold_act.setStatusTip('Toggle the font bold setting.')

        self.FontItalic_act = QAction("Toggle Italic", self)
        self.FontItalic_act.triggered.connect(self.onFontItalic)
        self.FontItalic_act.setStatusTip('Toggle the font italic setting.')

        self.FontSize_act = QAction("Font Size...", self)
        self.FontSize_act.triggered.connect(self.onFontSize)
        self.FontSize_act.setStatusTip('Set the font size.')

        self.SelectFont_act = QAction("Select Font...", self)
        self.SelectFont_act.triggered.connect(self.onSelectFont)
        self.SelectFont_act.setStatusTip('Select a the editor font.')

        self.SelectHighlightColor_act = QAction("Select Line Highlight Color...", self)
        self.SelectHighlightColor_act.triggered.connect(self.setHighlightColor)
        self.SelectHighlightColor_act.setStatusTip('Select a the editor line highlight color.')

        self.ResetHighlightColor_act = QAction("Reset Line Highlight Color", self)
        self.ResetHighlightColor_act.triggered.connect(self.resetHighlightColor)
        self.ResetHighlightColor_act.setStatusTip('Reset a the editor line highlight color to the default color.')

        self.SelectTheme_act = QAction("Select Theme...", self)
        self.SelectTheme_act.triggered.connect(self.SelectTheme)
        self.ResetHighlightColor_act.setStatusTip('Select from the current supported system themes.')

        options_menu.addAction(self.FontBold_act)
        options_menu.addAction(self.FontItalic_act)
        options_menu.addAction(self.FontSize_act)
        options_menu.addAction(self.SelectFont_act)
        options_menu.addAction(self.ResetFont_act)
        options_menu.addSeparator()
        options_menu.addAction(self.SelectHighlightColor_act)
        options_menu.addAction(self.ResetHighlightColor_act)
        options_menu.addSeparator()
        options_menu.addAction(self.SelectTheme_act)

        ###  Help Menu
        help_menu = self.inputpane.menu.addMenu("Help")

        self.help_act = QAction("Help...", self)
        self.help_act.triggered.connect(self.onHelp)
        self.help_act.setStatusTip('Help with ' + self.program_title + " Version " + self.version + "...")
        help_menu.addAction(self.help_act)

        self.help_about_act = QAction("About...", self)
        self.help_about_act.triggered.connect(self.aboutDialog)
        self.help_about_act.setStatusTip('About ' + self.program_title)
        help_menu.addAction(self.help_about_act)

        try:
            with open('TextConverterOptions.opt', 'rb') as f:
                filecontents = pickle.load(f)
                optList = GeneralOptions()
                optList.fromList(filecontents)
                doc = self.inputpane.editor.document()
                doc.setDefaultFont(optList.Font)
                self.inputpane.editor.setHighlightLineColor(optList.highlightColor)
                self.Parent.setStyle(optList.theme)
                self.currentTheme = optList.theme
        except Exception as e:
            pass

        self.setStatusBar(QStatusBar(self))

        try:
            if filetoload != '':
                f = open(filetoload, 'r')
                self.inputpane.editor.insertPlainText(f.read())
        except:
            pass

    def onNewWindow(self):
        self.newwindow = TextConverter()
        self.programList.append(self.newwindow)

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

    def SelectTheme(self):
        items = QStyleFactory.keys()
        if len(items) <= 1:
            return

        items.sort()
        item, ok = QInputDialog.getItem(self, "Select Theme", "Available Themes", items, 0, False)

        if ok:
            self.Parent.setStyle(item)
            self.currentTheme = item
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

    def resetHighlightColor(self):
        self.inputpane.editor.resetHighlightLineColor()
        self.saveOptions()
        self.inputpane.editor.highlight_current_line()

    def setHighlightColor(self):
        doc = self.inputpane.editor.document()
        col = self.inputpane.editor.highlight_line_color
        colordialog = QColorDialog(col)
        if colordialog.exec():
            col = colordialog.currentColor()
            self.inputpane.editor.setHighlightLineColor(col)
            self.saveOptions()
            self.inputpane.editor.highlight_current_line()

    def saveOptions(self):
        opts = GeneralOptions()
        doc = self.inputpane.editor.document()
        font = doc.defaultFont()
        hlcolor = self.inputpane.editor.highlight_line_color
        opts.Font = font
        opts.highlightColor = hlcolor
        opts.theme = self.currentTheme
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload = ''
    if (len(sys.argv) > 1):
        fileload = sys.argv[1]

    window = TextConverter(app, filetoload = fileload)
    progcss = appcss()
    app.setStyleSheet(progcss.getCSS())
    sys.exit(app.exec())
