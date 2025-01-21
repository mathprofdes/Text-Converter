#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created: 7/20/2024
Revised: 8/17/2024

@author: Don Spickler

Text area with numerous text and numeric conversion options.  String conversion and
manipulation options, character encodings and decodongs, numeric base conversions,
zero padding and removal, random number generation using several different distributions,
and C++ code string manipulations.

"""
import os
import random
import sys
from random import *

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtPrintSupport import *
from PySide6.QtWidgets import *

from BBSRandBitDialog import *
from BinomialRandDialog import *
from ExpRandDialog import *
from NormalRandDialog import *
from OneNumberInputDialog import *
from StringInputDialog import *
from TwoNumberInputDialog import *
from TwoStringInputDialog import *
from CharStreamBreakInputDialog import *
from UniformRandIntDialog import *

class InputPane(QWidget):

    def __init__(self, frame=True, title="Input", singleToolMenu = True, SpecialOps = True, CodeMenu=False, Shortcuts = True):
        """
        InputPane constructor

        :param Frame: bool to include a frame and title.
        :param title: str frame title if using a frame.
        :param singleToolMenu: bool to condense all tool menu options to submenus of a Tool menu.
        :param SpecialOps: bool to include special operations.
        :param CodeMenu: bool to include the C++ code menu.
        :param Shortcuts: bool to include some menu shortcuts.
        """
        super().__init__()
        self.title = title
        self.frame = frame
        self.condTools = singleToolMenu
        self.SpecialOperations = SpecialOps
        self.IncludeCodeMenu = CodeMenu
        self.IncludeShortcuts = Shortcuts
        self.clipboard = QApplication.clipboard()
        self.initializeUI()

    def initializeUI(self):
        """
        Sets up the user interface for the control.
        """
        self.menu = self.createMenu()
        self.editor = QPlainTextEdit()

        doc = self.editor.document()
        font = doc.defaultFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setPointSize(12)
        doc.setDefaultFont(font)

        pane_layout = QVBoxLayout()
        pane_layout.addWidget(self.menu)
        pane_layout.addWidget(self.editor)
        pane_layout.setContentsMargins(2, 2, 2, 2)

        if self.frame:
            pane_group = QGroupBox(self.title)
            pane_group.setLayout(pane_layout)
            app_form_layout = QFormLayout()
            app_form_layout.setContentsMargins(2, 2, 2, 2)
            app_form_layout.addRow(pane_group)
            self.setLayout(app_form_layout)
        else:
            self.setLayout(pane_layout)

    def getText(self):
        """ Returns the text in the editor. """
        return self.editor.toPlainText()

    def setText(self, str):
        """ Sets the text in the editor. """
        return self.editor.setPlainText(str)

    def createMenu(self):
        """
        Creates the menu for the editor controls.
        """
        # File Menu Actions
        self.file_new_act = QAction("New", self)
        if self.IncludeShortcuts:
            self.file_new_act.setShortcut('Ctrl+N')
        self.file_new_act.triggered.connect(self.newFile)

        self.file_open_act = QAction("Open...", self)
        if self.IncludeShortcuts:
            self.file_open_act.setShortcut('Ctrl+O')
        self.file_open_act.triggered.connect(self.openFile)

        self.file_saveas_act = QAction("Save As...", self)
        if self.IncludeShortcuts:
            self.file_saveas_act.setShortcut('Ctrl+S')
        self.file_saveas_act.triggered.connect(self.saveFileAs)

        self.file_print_act = QAction("Print...", self)
        if self.IncludeShortcuts:
            self.file_print_act.setShortcut('Ctrl+P')
        self.file_print_act.triggered.connect(self.print)

        self.file_PrintPreview_act = QAction("Print Preview...", self)
        self.file_PrintPreview_act.triggered.connect(self.printPreview)

        self.file_Stats_act = QAction("Statistics...", self)
        self.file_Stats_act.triggered.connect(self.showFileStats)

        # Edit Menu Actions
        self.edit_wrap_act = QAction("Toggle Word Wrap", self)
        if self.IncludeShortcuts:
            self.edit_wrap_act.setShortcut('Ctrl+W')
        self.edit_wrap_act.triggered.connect(self.ToggleWordWrap)

        self.edit_cut_act = QAction("Cut", self)
        if self.IncludeShortcuts:
            self.edit_cut_act.setShortcut('Ctrl+X')
        self.edit_cut_act.triggered.connect(self.cutText)

        self.edit_copy_act = QAction("Copy", self)
        if self.IncludeShortcuts:
            self.edit_copy_act.setShortcut('Ctrl+C')
        self.edit_copy_act.triggered.connect(self.copyText)

        self.edit_copyAll_act = QAction("Copy All", self)
        if self.IncludeShortcuts:
            self.edit_copyAll_act.setShortcut('Shift+Ctrl+C')
        self.edit_copyAll_act.triggered.connect(self.copyAllText)

        self.edit_paste_act = QAction("Paste", self)
        if self.IncludeShortcuts:
            self.edit_paste_act.setShortcut('Ctrl+V')
        self.edit_paste_act.triggered.connect(self.pasteText)

        self.edit_selectall_act = QAction("Select All", self)
        if self.IncludeShortcuts:
            self.edit_selectall_act.setShortcut('Ctrl+A')
        self.edit_selectall_act.triggered.connect(self.selectallText)

        self.edit_undo_act = QAction("Undo", self)
        if self.IncludeShortcuts:
            self.edit_undo_act.setShortcut('Ctrl+Z')
        self.edit_undo_act.triggered.connect(self.undoText)

        self.edit_redo_act = QAction("Redo", self)
        if self.IncludeShortcuts:
            self.edit_redo_act.setShortcut('Ctrl+Shift+Z')
        self.edit_redo_act.triggered.connect(self.redoText)

        # Tool String Menu Actions
        self.tool_string_toupper_act = QAction("UPPERCASE", self)
        self.tool_string_toupper_act.triggered.connect(self.toupper)

        self.tool_string_tolower_act = QAction("lowercase", self)
        self.tool_string_tolower_act.triggered.connect(self.tolower)

        self.tool_string_tocaps_act = QAction("Capitalize", self)
        self.tool_string_tocaps_act.triggered.connect(self.tocaps)

        self.tool_string_removeWS_act = QAction("Remove All Whitespace", self)
        self.tool_string_removeWS_act.triggered.connect(self.remAllWS)

        self.tool_string_removeWSperLine_act = QAction("Remove Whitespace Per Line", self)
        self.tool_string_removeWSperLine_act.triggered.connect(self.remWSperLine)

        self.tool_string_removeWStoSpace_act = QAction("Whitespace to Single Spaces", self)
        self.tool_string_removeWStoSpace_act.triggered.connect(self.remWStoSingleSpace)

        self.tool_string_removePunct_act = QAction("Remove Punctuation", self)
        self.tool_string_removePunct_act.triggered.connect(self.remPunct)

        self.tool_string_removeNumbers_act = QAction("Remove Numbers", self)
        self.tool_string_removeNumbers_act.triggered.connect(self.remNumbers)

        self.tool_string_removeNonLetters_act = QAction("Remove All Non-Letters", self)
        self.tool_string_removeNonLetters_act.triggered.connect(self.remNonLetters)

        self.tool_string_split_act = QAction("Split (Spaces to Line Breaks)", self)
        self.tool_string_split_act.triggered.connect(self.splitAct)

        self.tool_string_join_act = QAction("Join (Line Breaks to Spaces)", self)
        self.tool_string_join_act.triggered.connect(self.joinAct)

        self.tool_string_removeBlankLines_act = QAction("Remove All Blank Lines", self)
        self.tool_string_removeBlankLines_act.triggered.connect(self.remBlankLines)

        self.tool_string_removeMultipleBlankLines_act = QAction("Remove Multiple Blank Lines", self)
        self.tool_string_removeMultipleBlankLines_act.triggered.connect(self.remMultipleBlankLines)

        self.tool_string_removeFrontWS_act = QAction("Remove Front Whitespace", self)
        self.tool_string_removeFrontWS_act.triggered.connect(self.remFrontWS)

        self.tool_string_removeEndWS_act = QAction("Remove End Whitespace", self)
        self.tool_string_removeEndWS_act.triggered.connect(self.remEndWS)

        self.tool_string_TrimLines_act = QAction("Trim Lines", self)
        self.tool_string_TrimLines_act.triggered.connect(self.trimAllLines)

        self.tool_string_ReplaceAll_act = QAction("Replace All...", self)
        self.tool_string_ReplaceAll_act.triggered.connect(self.replaceALL)

        self.tool_string_SplitAt_act = QAction("Split At...", self)
        self.tool_string_SplitAt_act.triggered.connect(self.splitAt)

        self.tool_string_BreakCharStream_act = QAction("Break Character Stream...", self)
        self.tool_string_BreakCharStream_act.triggered.connect(self.breakCharStream)

        self.tool_string_ReformatCharStream_act = QAction("Reformat Text...", self)
        self.tool_string_ReformatCharStream_act.triggered.connect(self.reformatCharStream)

        self.tool_string_RemoveDoubleChars_act = QAction("Remove Double Characters", self)
        self.tool_string_RemoveDoubleChars_act.triggered.connect(self.RemoveDoubleChars)

        # Tool Character Menu Actions
        self.tool_char_AZ_1_26_act = QAction("A-Z -> 1-26", self)
        self.tool_char_AZ_1_26_act.triggered.connect(self.AZ_1_26)

        self.tool_char_AZ_01_26_act = QAction("A-Z -> 01-26", self)
        self.tool_char_AZ_01_26_act.triggered.connect(self.AZ_01_26)

        self.tool_char_AZ_0_25_act = QAction("A-Z -> 0-25", self)
        self.tool_char_AZ_0_25_act.triggered.connect(self.AZ_0_25)

        self.tool_char_AZ_00_25_act = QAction("A-Z -> 00-25", self)
        self.tool_char_AZ_00_25_act.triggered.connect(self.AZ_00_25)

        self.tool_char_AZ_1_26B_act = QAction("A-Z -> 1-26:  Binary", self)
        self.tool_char_AZ_1_26B_act.triggered.connect(self.AZ_1_26B)

        self.tool_char_AZ_0_25B_act = QAction("A-Z -> 0-25:  Binary", self)
        self.tool_char_AZ_0_25B_act.triggered.connect(self.AZ_0_25B)

        self.tool_char_AZ_1_26B_8_act = QAction("A-Z -> 1-26:  8-Bit Binary", self)
        self.tool_char_AZ_1_26B_8_act.triggered.connect(self.AZ_1_26B_8)

        self.tool_char_AZ_0_25B_8_act = QAction("A-Z -> 0-25:  8-Bit Binary", self)
        self.tool_char_AZ_0_25B_8_act.triggered.connect(self.AZ_0_25B_8)

        self.tool_Text_Ascii_act = QAction("Text -> ASCII", self)
        self.tool_Text_Ascii_act.triggered.connect(self.TextASCII)

        self.tool_Text_Ascii3_act = QAction("Text -> ASCII:  3-Digits", self)
        self.tool_Text_Ascii3_act.triggered.connect(self.TextASCII3)

        self.tool_Text_AsciiB_act = QAction("Text -> ASCII:  Binary", self)
        self.tool_Text_AsciiB_act.triggered.connect(self.TextASCIIB)

        self.tool_Text_AsciiB_8_act = QAction("Text -> ASCII:  8-Bit Binary", self)
        self.tool_Text_AsciiB_8_act.triggered.connect(self.TextASCIIB_8)

        self.tool_char_1_26_AZ_act = QAction("1-26 -> A-Z", self)
        self.tool_char_1_26_AZ_act.triggered.connect(self.Conv_1_26_AZ)

        self.tool_char_0_25_AZ_act = QAction("0-25 -> A-Z", self)
        self.tool_char_0_25_AZ_act.triggered.connect(self.Conv_0_25_AZ)

        self.tool_char_1_26B_AZ_act = QAction("1-26 Binary -> A-Z", self)
        self.tool_char_1_26B_AZ_act.triggered.connect(self.Conv_1_26B_AZ)

        self.tool_char_0_25B_AZ_act = QAction("0-25 Binary -> A-Z", self)
        self.tool_char_0_25B_AZ_act.triggered.connect(self.Conv_0_25B_AZ)

        self.tool_Ascii_Text_act = QAction("ASCII -> Text", self)
        self.tool_Ascii_Text_act.triggered.connect(self.ASCIIText)

        self.tool_AsciiB_Text_act = QAction("ASCII Binary -> Text", self)
        self.tool_AsciiB_Text_act.triggered.connect(self.ASCIIBText)

        # Tool Numeric Conversions Menu Actions
        self.tool_num_BaseConv_act = QAction("General Base Conversion...", self)
        self.tool_num_BaseConv_act.triggered.connect(self.ConvertBaseGen)

        self.tool_num_10_2_act = QAction("Decimal -> Binary", self)
        self.tool_num_10_2_act.triggered.connect(self.Convert_10_2)

        self.tool_num_10_8_act = QAction("Decimal -> Octal", self)
        self.tool_num_10_8_act.triggered.connect(self.Convert_10_8)

        self.tool_num_10_16_act = QAction("Decimal -> Hexadecimal", self)
        self.tool_num_10_16_act.triggered.connect(self.Convert_10_16)

        self.tool_num_2_8_act = QAction("Binary -> Octal", self)
        self.tool_num_2_8_act.triggered.connect(self.Convert_2_8)

        self.tool_num_2_10_act = QAction("Binary -> Decimal", self)
        self.tool_num_2_10_act.triggered.connect(self.Convert_2_10)

        self.tool_num_2_16_act = QAction("Binary -> Hexadecimal", self)
        self.tool_num_2_16_act.triggered.connect(self.Convert_2_16)

        self.tool_num_8_2_act = QAction("Octal -> Binary", self)
        self.tool_num_8_2_act.triggered.connect(self.Convert_8_2)

        self.tool_num_8_10_act = QAction("Octal -> Decimal", self)
        self.tool_num_8_10_act.triggered.connect(self.Convert_8_10)

        self.tool_num_8_16_act = QAction("Octal -> Hexadecimal", self)
        self.tool_num_8_16_act.triggered.connect(self.Convert_8_16)

        self.tool_num_16_2_act = QAction("Hexadecimal -> Binary", self)
        self.tool_num_16_2_act.triggered.connect(self.Convert_16_2)

        self.tool_num_16_8_act = QAction("Hexadecimal -> Octal", self)
        self.tool_num_16_8_act.triggered.connect(self.Convert_16_8)

        self.tool_num_16_10_act = QAction("Hexadecimal -> Decimal", self)
        self.tool_num_16_10_act.triggered.connect(self.Convert_16_10)

        self.tool_num_RemoveZeros_act = QAction("Remove Leading Zeros", self)
        self.tool_num_RemoveZeros_act.triggered.connect(self.RemoveZeros)

        self.tool_num_RemoveZeros_MinLength_act = QAction("Remove Leading Zeros with Minimum Length...", self)
        self.tool_num_RemoveZeros_MinLength_act.triggered.connect(self.RemoveZerosMinLength)

        self.tool_num_PadZeros_act = QAction("Pad with Zeros...", self)
        self.tool_num_PadZeros_act.triggered.connect(self.PadZeros)

        self.tool_code_TabSpace1_act = QAction("1 Space", self)
        self.tool_code_TabSpace1_act.triggered.connect(self.ConvertTabSpace1)

        self.tool_code_TabSpace2_act = QAction("2 Spaces", self)
        self.tool_code_TabSpace2_act.triggered.connect(self.ConvertTabSpace2)

        self.tool_code_TabSpace3_act = QAction("3 Spaces", self)
        self.tool_code_TabSpace3_act.triggered.connect(self.ConvertTabSpace3)

        self.tool_code_TabSpace4_act = QAction("4 Spaces", self)
        self.tool_code_TabSpace4_act.triggered.connect(self.ConvertTabSpace4)

        self.tool_code_TabSpace5_act = QAction("5 Spaces", self)
        self.tool_code_TabSpace5_act.triggered.connect(self.ConvertTabSpace5)

        self.tool_code_SpaceTab_act = QAction("Convert Spaces to Tabs", self)
        self.tool_code_SpaceTab_act.triggered.connect(self.ConvertSpaceTab)

        self.tool_code_RemoveComments_act = QAction("Remove C++/Java Style Comments", self)
        self.tool_code_RemoveComments_act.triggered.connect(self.RemoveComments)

        self.tool_code_CodeString_act = QAction("Convert to C++ Code String", self)
        self.tool_code_CodeString_act.triggered.connect(self.ConvertToCodeString)

        self.tool_code_Condense_act = QAction("Condense", self)
        self.tool_code_Condense_act.triggered.connect(self.Condense)

        self.tool_code_CondenseConvert_act = QAction("Condense and Convert to C++ Code String", self)
        self.tool_code_CondenseConvert_act.triggered.connect(self.CondenseConvert)

        # Random Number Menu Actions
        self.tool_rand_Int_act = QAction("Uniform Integer Range...", self)
        self.tool_rand_Int_act.triggered.connect(self.RandIntRange)

        self.tool_rand_Float_act = QAction("Uniform Float Range...", self)
        self.tool_rand_Float_act.triggered.connect(self.RandFloatRange)

        self.tool_rand_Binomial_act = QAction("Binomial Distribution...", self)
        self.tool_rand_Binomial_act.triggered.connect(self.RandBinomial)

        self.tool_rand_Normal_act = QAction("Normal Distribution...", self)
        self.tool_rand_Normal_act.triggered.connect(self.RandNormal)

        self.tool_rand_LogNormal_act = QAction("Log Normal Distribution...", self)
        self.tool_rand_LogNormal_act.triggered.connect(self.RandLogNormal)

        self.tool_rand_ExpDist_act = QAction("Exponential Distribution...", self)
        self.tool_rand_ExpDist_act.triggered.connect(self.RandExp)

        self.tool_rand_BBS_act = QAction("Blum-Blum-Shub Bit Generator...", self)
        self.tool_rand_BBS_act.triggered.connect(self.RandBBS)

        # Create the menu bar
        menu_bar = QMenuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions
        self.file_menu = menu_bar.addMenu('File')
        self.file_menu.addAction(self.file_new_act)
        self.file_menu.addAction(self.file_open_act)
        self.file_menu.addAction(self.file_saveas_act)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.file_print_act)
        self.file_menu.addAction(self.file_PrintPreview_act)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.file_Stats_act)

        # Create edit menu and add actions
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(self.edit_cut_act)
        edit_menu.addAction(self.edit_copy_act)
        edit_menu.addAction(self.edit_copyAll_act)
        edit_menu.addAction(self.edit_paste_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.edit_selectall_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.edit_undo_act)
        edit_menu.addAction(self.edit_redo_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.edit_wrap_act)

        # Create string conversions submenu and add actions
        if self.condTools:
            tool_menu = menu_bar.addMenu('Tools')
            string_menu = tool_menu.addMenu('String Conversions')
        else:
            string_menu = menu_bar.addMenu('Strings')

        string_menu.addAction(self.tool_string_toupper_act)
        string_menu.addAction(self.tool_string_tolower_act)
        string_menu.addAction(self.tool_string_tocaps_act)
        string_menu.addSeparator()
        string_menu.addAction(self.tool_string_removeWS_act)
        string_menu.addAction(self.tool_string_removeWStoSpace_act)
        string_menu.addAction(self.tool_string_removeWSperLine_act)
        string_menu.addAction(self.tool_string_removePunct_act)
        string_menu.addAction(self.tool_string_removeNumbers_act)
        string_menu.addAction(self.tool_string_removeNonLetters_act)
        string_menu.addSeparator()
        string_menu.addAction(self.tool_string_split_act)
        string_menu.addAction(self.tool_string_join_act)
        string_menu.addAction(self.tool_string_removeBlankLines_act)
        string_menu.addAction(self.tool_string_removeMultipleBlankLines_act)
        string_menu.addSeparator()
        string_menu.addAction(self.tool_string_removeFrontWS_act)
        string_menu.addAction(self.tool_string_removeEndWS_act)
        string_menu.addAction(self.tool_string_TrimLines_act)
        string_menu.addSeparator()

        tabspacemenu = string_menu.addMenu("Convert Tabs to Spaces")
        tabspacemenu.addAction(self.tool_code_TabSpace1_act)
        tabspacemenu.addAction(self.tool_code_TabSpace2_act)
        tabspacemenu.addAction(self.tool_code_TabSpace3_act)
        tabspacemenu.addAction(self.tool_code_TabSpace4_act)
        tabspacemenu.addAction(self.tool_code_TabSpace5_act)

        string_menu.addAction(self.tool_code_SpaceTab_act)
        string_menu.addSeparator()
        string_menu.addAction(self.tool_string_ReplaceAll_act)
        string_menu.addAction(self.tool_string_SplitAt_act)
        string_menu.addAction(self.tool_string_BreakCharStream_act)
        string_menu.addAction(self.tool_string_ReformatCharStream_act)
        if self.SpecialOperations:
            string_menu.addSeparator()
            string_menu.addAction(self.tool_string_RemoveDoubleChars_act)

        # Create character coding submenu and add actions
        if self.condTools:
            char_menu = tool_menu.addMenu('Character Coding')
        else:
            char_menu = menu_bar.addMenu('Characters')

        char_menu.addAction(self.tool_char_AZ_1_26_act)
        char_menu.addAction(self.tool_char_AZ_01_26_act)
        char_menu.addAction(self.tool_char_AZ_0_25_act)
        char_menu.addAction(self.tool_char_AZ_00_25_act)
        char_menu.addSeparator()
        char_menu.addAction(self.tool_char_AZ_1_26B_act)
        char_menu.addAction(self.tool_char_AZ_0_25B_act)
        char_menu.addAction(self.tool_char_AZ_1_26B_8_act)
        char_menu.addAction(self.tool_char_AZ_0_25B_8_act)
        char_menu.addSeparator()
        char_menu.addAction(self.tool_Text_Ascii_act)
        char_menu.addAction(self.tool_Text_Ascii3_act)
        char_menu.addAction(self.tool_Text_AsciiB_act)
        char_menu.addAction(self.tool_Text_AsciiB_8_act)
        char_menu.addSeparator()
        char_menu.addAction(self.tool_char_1_26_AZ_act)
        char_menu.addAction(self.tool_char_0_25_AZ_act)
        char_menu.addAction(self.tool_char_1_26B_AZ_act)
        char_menu.addAction(self.tool_char_0_25B_AZ_act)
        char_menu.addSeparator()
        char_menu.addAction(self.tool_Ascii_Text_act)
        char_menu.addAction(self.tool_AsciiB_Text_act)

        # Create numeric conversion submenu and add actions
        if self.condTools:
            num_menu = tool_menu.addMenu('Numeric Conversions')
        else:
            num_menu = menu_bar.addMenu('Numbers')

        num_menu.addAction(self.tool_num_10_2_act)
        num_menu.addAction(self.tool_num_10_8_act)
        num_menu.addAction(self.tool_num_10_16_act)
        num_menu.addSeparator()
        num_menu.addAction(self.tool_num_2_8_act)
        num_menu.addAction(self.tool_num_2_10_act)
        num_menu.addAction(self.tool_num_2_16_act)
        num_menu.addSeparator()
        num_menu.addAction(self.tool_num_8_2_act)
        num_menu.addAction(self.tool_num_8_10_act)
        num_menu.addAction(self.tool_num_8_16_act)
        num_menu.addSeparator()
        num_menu.addAction(self.tool_num_16_2_act)
        num_menu.addAction(self.tool_num_16_8_act)
        num_menu.addAction(self.tool_num_16_10_act)
        num_menu.addSeparator()
        num_menu.addAction(self.tool_num_BaseConv_act)
        num_menu.addSeparator()
        num_menu.addAction(self.tool_num_RemoveZeros_act)
        num_menu.addAction(self.tool_num_RemoveZeros_MinLength_act)
        num_menu.addAction(self.tool_num_PadZeros_act)

        # Create random number generator submenu and add actions
        if self.condTools:
            rand_menu = tool_menu.addMenu('Random Numbers')
        else:
            rand_menu = menu_bar.addMenu('Random')

        rand_menu.addAction(self.tool_rand_Int_act)
        rand_menu.addAction(self.tool_rand_Float_act)
        rand_menu.addSeparator()
        rand_menu.addAction(self.tool_rand_Binomial_act)
        rand_menu.addSeparator()
        rand_menu.addAction(self.tool_rand_Normal_act)
        rand_menu.addAction(self.tool_rand_LogNormal_act)
        rand_menu.addAction(self.tool_rand_ExpDist_act)
        rand_menu.addSeparator()
        rand_menu.addAction(self.tool_rand_BBS_act)

        # Create code conversion submenu and add actions
        if self.IncludeCodeMenu:
            if self.condTools:
                code_menu = tool_menu.addMenu('Code Conversions')
            else:
                code_menu = menu_bar.addMenu('Code')

            code_menu.addAction(self.tool_code_RemoveComments_act)
            code_menu.addAction(self.tool_code_CodeString_act)
            code_menu.addSeparator()
            code_menu.addAction(self.tool_code_Condense_act)
            code_menu.addAction(self.tool_code_CondenseConvert_act)

        return menu_bar

    def updateEditor(self, str):
        """
        Updates the editor with input test and adds the contents to the undo/redo stack.
        """
        self.editor.selectAll()
        self.editor.cut()
        self.editor.appendPlainText(str)

    def newFile(self):
        """ Clears the editor area. """
        gotClipContents = True
        try:
            ctext = self.clipboard.text()
        except:
            gotClipContents = False
            ctext = ""

        self.editor.selectAll()
        self.editor.cut()
        if gotClipContents:
            self.clipboard.setText(ctext)

    def openFile(self):
        """ Open and loads a text file. """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*.*)")

        if file_name != "":
            f = open(file_name, 'r')
            self.updateEditor(f.read())

    def saveFileAs(self):
        """ Saves the contents of the editor to a text file. """
        dialog = QFileDialog(self)
        dialog.setFilter(dialog.filter() | QDir.Hidden)
        dialog.setDefaultSuffix('txt')
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setNameFilters(['Text Files (*.txt)', 'All Files (*.*)'])
        dialog.setWindowTitle('Save As')

        if dialog.exec() == QDialog.Accepted:
            filelist = dialog.selectedFiles()
            if len(filelist) > 0:
                file_name = filelist[0]
                f = open(file_name, 'w')
                f.write(self.editor.toPlainText())

    def print(self):
        """ Prints the contents of the editor to the selected printer. """
        printer = QPrinter()
        dialog = QPrintDialog(printer, self)
        printer.setDocName("Editor_Document")
        printer.setResolution(300)
        if dialog.exec() == QDialog.Accepted:
            self.editor.print_(printer)

    def printPreview(self):
        """ Prints the contents of the editor to a print preview dialog. """
        printer = QPrinter()
        dialog = QPrintPreviewDialog(printer, self)
        printer.setDocName("Editor_Document")
        printer.setResolution(300)
        dialog.paintRequested.connect(self.printPreviewDoc)
        dialog.exec()

    def printPreviewDoc(self, printer):
        """ Print function to link to preview system. """
        self.editor.print_(printer)

    def showFileStats(self):
        """ Calculates and reports some basic statistics of the editor content. """
        edstr = self.editor.toPlainText()
        charcount = len(edstr)
        nwsstr = self.removeAllWhitespace(edstr)
        charcountNWS = len(nwsstr)
        wordstr = self.WStoSingleSpace(edstr)
        wordlist = wordstr.split(' ')
        wordcount = len(wordlist)
        if wordcount == 1 and len(wordlist[0].strip()) == 0:
            wordcount = 0
        message = "Characters: " + str(charcount) + "\n"
        message += "Characters (no spaces): " + str(charcountNWS) + "\n"
        message += "Words: " + str(wordcount) + "\n"
        QMessageBox.information(self, "Document Statistics", message, QMessageBox.Ok)

    def ToggleWordWrap(self):
        """ Toggles the word wrap state of the editor.  """
        wrapmode = self.editor.wordWrapMode()
        if wrapmode == QTextOption.WrapMode.NoWrap:
            self.editor.setWordWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
        else:
            self.editor.setWordWrapMode(QTextOption.WrapMode.NoWrap)

    def cutText(self):
        """ Cuts the selected test. """
        self.editor.cut()

    def copyText(self):
        """ Copies the selected text.  """
        self.editor.copy()

    def copyAllText(self):
        """ Copies all the editor text to the system clipboard. """
        self.clipboard.setText(self.editor.toPlainText())

    def pasteText(self):
        """ Pastes the clipboard text to the editor. """
        self.editor.paste()

    def selectallText(self):
        """ Selects all the text in the editor. """
        self.editor.selectAll()

    def undoText(self):
        """ Loads the previous edit fron the undo/redo stack. """
        self.editor.undo()

    def redoText(self):
        """ Loads the next edit fron the undo/redo stack. """
        self.editor.redo()

    def toupper(self):
        """ Converts all text in the editor to uppercase. """
        str = self.editor.toPlainText()
        self.updateEditor(str.upper())

    def tolower(self):
        """ Converts all text in the editor to lowercase. """
        str = self.editor.toPlainText()
        self.updateEditor(str.lower())

    def tocaps(self):
        """ Capitalizes each word in the editor. """
        str = self.editor.toPlainText()
        retstr = ""
        pos = 0
        lastpos = 0
        while pos < len(str):
            if str[pos].isspace():
                word = str[lastpos:pos]
                word = word.capitalize()
                retstr += word + str[pos]
                lastpos = pos + 1
            pos += 1

        if lastpos < pos:
            word = str[lastpos:pos]
            word = word.capitalize()
            retstr += word
        self.updateEditor(retstr)

    def removeAllWhitespace(self, str):
        """ Removes all whitespace characters from the input string. """
        repstr = ""
        for i in range(len(str)):
            if not str[i].isspace():
                repstr += str[i]
        return repstr

    def remAllWS(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.removeAllWhitespace(self.editor.toPlainText()))

    def removeWhitespacePerLine(self, str):
        """ Removes all whitespace characters from the input string line by line. """
        strlist = str.split('\n')
        repstr = ""
        for i in range(len(strlist)):
            repstr += self.removeAllWhitespace(strlist[i]) + '\n'
        return repstr.strip()

    def remWSperLine(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.removeWhitespacePerLine(self.editor.toPlainText()))

    def WStoSingleSpace(self, str):
        """ Converts all whitespace to single spaces. """
        repstr = ""
        for i in range(len(str)):
            if str[i].isspace():
                if i > 0 and not str[i - 1].isspace():
                    repstr += " "
            else:
                repstr += str[i]
        repstr = repstr.strip()
        return repstr

    def WStoSpace(self, str):
        """ Converts all whitespace characters to spaces. """
        repstr = ""
        for i in range(len(str)):
            if str[i].isspace():
                repstr += " "
            else:
                repstr += str[i]
        return repstr

    def splitString(self, str):
        """ Splits the string by converting spaces to new line characters. """
        repstr = self.WStoSpace(str)
        return repstr.replace(' ', '\n')

    def joinString(self, str):
        """ Joins the string by converting new line characters to spaces. """
        return str.replace('\n', ' ')

    def removeBlankLines(self, str):
        """ Removes all blank lines from the string. """
        strlist = str.split('\n')
        repstr = ""
        for i in range(len(strlist)):
            tstr = strlist[i].strip()
            if len(tstr) > 0:
                repstr += strlist[i] + '\n'
        return repstr.strip()

    def removeMultipleBlankLines(self, str):
        """ Removes all multiple blank lines from the string and replaces by a single blank line. """
        strlist = str.split('\n')
        repstr = ""
        for i in range(len(strlist)):
            if i > 0:
                laststr = strlist[i-1].strip()
                tstr = strlist[i].strip()
                if len(tstr) > 0 or len(laststr) > 0:
                    repstr += strlist[i] + '\n'
            else:
                repstr += strlist[i] + '\n'
        return repstr.strip()

    def trimLines(self, str, trimfront=True, trimback=True):
        """
        Removes leading and trailing whitespace from each line, depending on the trimfront and trimback values.
        """
        strlist = str.split('\n')
        repstr = ""
        for i in range(len(strlist)):
            newline = strlist[i]
            if trimfront:
                newline = newline.lstrip()
            if trimback:
                newline = newline.rstrip()
            repstr += newline + '\n'
        return repstr

    def remWStoSingleSpace(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.WStoSingleSpace(self.editor.toPlainText()))

    def remPunct(self):
        """ Removes all punctuation from the string. """
        str = self.editor.toPlainText()
        repstr = ""
        for i in range(len(str)):
            if str[i].isalnum() or str[i].isspace():
                repstr += str[i]
        self.updateEditor(repstr)

    def remNumbers(self):
        """ Removes all numbers from the string. """
        str = self.editor.toPlainText()
        repstr = ""
        for i in range(len(str)):
            if not str[i].isdigit():
                repstr += str[i]
        self.updateEditor(repstr)

    def remNonLetters(self):
        """ Removes all non-letters from the string. """
        str = self.editor.toPlainText()
        repstr = ""
        for i in range(len(str)):
            if str[i].isalpha() or str[i].isspace():
                repstr += str[i]
        self.updateEditor(repstr)

    def RemoveDoubleChars(self):
        """
        Special function to break multiple letters, e.g food to foXod.  Used in some classical cryptographic
        processes.
        """
        str = self.editor.toPlainText()
        repstr = ""
        for i in range(len(str)):
            if i > 0 and str[i-1] == str[i]:
                if str[i] != 'X':
                    repstr += 'X' + str[i]
                else:
                    repstr += 'Z' + str[i]
            else:
                repstr += str[i]
        self.updateEditor(repstr)

    def splitAct(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.splitString(self.editor.toPlainText()))

    def joinAct(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.joinString(self.editor.toPlainText()))

    def remBlankLines(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.removeBlankLines(self.editor.toPlainText()))

    def remMultipleBlankLines(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.removeMultipleBlankLines(self.editor.toPlainText()))

    def remFrontWS(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.trimLines(self.editor.toPlainText(), True, False))

    def remEndWS(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.trimLines(self.editor.toPlainText(), False, True))

    def trimAllLines(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.trimLines(self.editor.toPlainText()))

    def replaceALL(self):
        """ String replacement function with dialog interface. """
        dialog = TwoStringInputDialog(self, "Replace All", "Input target and replacement strings.", "Target:",
                                      "Replacement:", 200)
        if dialog.exec():
            self.updateEditor(self.editor.toPlainText().replace(dialog.getText1(), dialog.getText2()))

    def splitAt(self):
        """ String split function with dialog interface. """
        dialog = StringInputDialog(self, "Split At", "Input string to use a split delimiter.", "Split String:",
                                   200)
        if dialog.exec():
            strlist = self.editor.toPlainText().split(dialog.getText())
            retstr = ""
            for str in strlist:
                retstr += str + '\n'
            self.updateEditor(retstr)

    def charStreamBreak(self, str, numChars, joinLines, presWords):
        """
        Function to break the string into lines of numChars maximum length.
        The joinLines bool designates if the text lines are joined before the split.
        The presWords bool designates if words are not to be split.
        """
        retstr = ""

        if joinLines:
            str = self.WStoSingleSpace(str)

        linelist = str.split('\n')

        for rest in linelist:
            rest = rest.strip()
            if presWords:
                while len(rest) > numChars:
                    pos = numChars
                    while pos >= 0 and not rest[pos].isspace():
                        pos -= 1
                    if pos > 0:
                        retstr += rest[0:pos].strip() + "\n"
                        rest = rest[pos:].strip()
                    else:
                        pos = numChars
                        while pos < len(rest) and not rest[pos].isspace():
                            pos += 1
                        if pos < len(rest):
                            retstr += rest[0:pos].strip() + "\n"
                            rest = rest[pos:].strip()
                        else:
                            retstr += rest + "\n"
                            rest = ""
            else:
                while len(rest) > numChars:
                    retstr += rest[0:numChars].strip() + "\n"
                    rest = rest[numChars:].strip()

            if len(rest) > 0:
                retstr += rest.strip() + "\n"

        return retstr.strip()

    def breakCharStream(self):
        """ Break character stream dialog interface for the stream break function. """
        dialog = CharStreamBreakInputDialog(self)
        if dialog.exec():
            self.updateEditor(
                self.charStreamBreak(self.editor.toPlainText(), dialog.getNum(), False, dialog.getPreserveWords()))

    def reformatCharStream(self):
        """ Reformatting dialog interface for the stream break function. """
        title = "Reformat Text"
        message = "Specify the maximum number of characters per line."
        lableMessage = "Characters:"
        dialog = CharStreamBreakInputDialog(self, title, message, lableMessage, False)
        if dialog.exec():
            self.updateEditor(self.charStreamBreak(self.editor.toPlainText(), dialog.getNum(), True, True))

    def baseConvert(self, num, oldbase, newbase):
        """ Base conversion of num from oldbase to newbase. """
        try:
            digstr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            digits = {c: i for i, c in enumerate(digstr)}
            deceq = 0
            if oldbase == 10:
                deceq = int(num)
            else:
                for i, digit in enumerate(reversed(num.upper())):
                    deceq += digits[digit] * (oldbase ** i)

            if newbase == 10:
                return str(deceq).strip()
            else:
                newbaselst = []
                while deceq > 0:
                    newbaselst.append(deceq % newbase)
                    deceq = deceq // newbase

                newbasestr = ""
                for ind in reversed(newbaselst):
                    newbasestr += digstr[ind]

                retstr = newbasestr.strip()
                if len(retstr) == 0:
                    retstr = '0'
                return retstr
        except:
            return ''

    def ConvertBaseGenString(self, istr, oldbase, newbase):
        """ Converts numeric stings in istr from the oldbase to the newbase. """
        repstr = ""
        for i in range(len(istr)):
            if istr[i].isalnum() or istr[i].isspace():
                repstr += istr[i]
        istr = self.WStoSingleSpace(repstr)
        numlist = istr.split(' ')
        totalString = ""
        for num in numlist:
            num = num.strip()
            newnumstr = self.baseConvert(num, oldbase, newbase)
            totalString += newnumstr + " "
        return totalString.strip()

    def ConvertBaseGen(self):
        """ Base conversion dialog for user input of conversion parameters. """
        dialog = TwoNumberInputDialog(self, "Input the Bases",
                                      "Input the original base and \nthe new base for conversion.", "Original Base:",
                                      "New Base:", 2, 36, 10, 2, 36, 10, 75)
        if dialog.exec():
            oldbase = dialog.getVal1()
            newbase = dialog.getVal2()
            istr = self.editor.toPlainText()
            self.updateEditor(self.ConvertBaseGenString(istr, oldbase, newbase))

    def charCode(self, istr, shift=0, pad=0, asciiout=False, binary=False):
        """
        Character coding to numbers of the contents of istr.
        :param shift: numeric shift after coding.
        :param pad: zero padding to maximum length.
        :param asciiout: use ascii/unicode values.
        :param binary: output is to be in binary form.
        """
        ostr = ""
        outlist = []
        if asciiout:
            for ch in istr:
                outlist.append(ord(ch) + shift)
        else:
            istr = istr.upper()
            for ch in istr:
                if ch.isalpha():
                    outlist.append(ord(ch) - ord('A') + shift)

        for val in outlist:
            valstr = str(val)
            if binary:
                valstr = self.baseConvert(valstr, 10, 2)
            ostr += self.zeropad(valstr, pad) + ' '

        return ostr

    def charDecode(self, istr, shift=0, asciiin=False, binary=False):
        """
        Character decoding to numbers of the contents of istr.
        :param shift: numeric shift after coding.
        :param asciiin: use ascii/unicode values.
        :param binary: output is to be in binary form.
        """
        istr = self.WStoSingleSpace(istr)
        inlist = istr.split(' ')
        numlist = []
        for valstr in inlist:
            try:
                val = int(valstr)
                if binary:
                    val = int(self.baseConvert(valstr, 2, 10))
                numlist.append(val - shift)
            except:
                pass

        ostr = ""
        outlist = []
        for num in numlist:
            try:
                if asciiin:
                    outlist.append(chr(num))
                else:
                    outlist.append(chr(num + ord('A')))
            except:
                pass

        for chstr in outlist:
            ostr += chstr # + ' '

        return ostr

    def zeropad(self, num, pad):
        """ Pad num string with zeros up to pad length. """
        while len(num) < pad:
            num = '0' + num
        return num

    def PadZeros(self):
        """
        Dialog interface for the zero padding function.
        """
        dialog = OneNumberInputDialog(self, "Pad Length",
                                      "Input the minimum string length for padding.", "Pad Length:",
                                      0, 1000, 8, 75)
        if dialog.exec():
            padlength = dialog.getVal()
            istr = self.editor.toPlainText()
            istr = self.WStoSingleSpace(istr)
            numlist = istr.split(' ')
            retstr = ''
            for num in numlist:
                retstr += self.zeropad(num, padlength) + ' '
            self.updateEditor(retstr.strip())

    def stripLeadingZeros(self, istr, minlen = 0):
        """ Removes leading zeros down to minlen size. """
        istr = self.WStoSingleSpace(istr)
        numlist = istr.split(' ')
        retstr = ''
        for num in numlist:
            while len(num) > minlen and num[0] == '0':
                num = num[1:]
            if len(num) == 0:
                num = '0'
            retstr += num + ' '
        return retstr.strip()

    def RemoveZeros(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.stripLeadingZeros(self.editor.toPlainText(), 0))

    def RemoveZerosMinLength(self):
        """ Dialog interface for leading zero removal. """
        dialog = OneNumberInputDialog(self, "Minimum Length",
                                      "Input the minimum string length to retain.", "Minimum Length:",
                                      0, 1000, 8, 75)
        if dialog.exec():
            self.updateEditor(self.stripLeadingZeros(self.editor.toPlainText(), dialog.getVal()))

    def AZ_1_26(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 1, 0))

    def AZ_0_25(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 0, 0))

    def AZ_01_26(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 1, 2))

    def AZ_00_25(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 0, 2))

    def AZ_1_26B(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 1, 0, False, True))

    def AZ_0_25B(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 0, 0, False, True))

    def AZ_1_26B_8(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 1, 8, False, True))

    def AZ_0_25B_8(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 0, 8, False, True))

    def TextASCII(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 0, 0, True))

    def TextASCIIB(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 0, 0, True, True))

    def TextASCIIB_8(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 0, 8, True, True))

    def TextASCII3(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charCode(self.editor.toPlainText(), 0, 3, True))

    def Conv_1_26_AZ(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charDecode(self.editor.toPlainText(), 1))

    def Conv_0_25_AZ(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charDecode(self.editor.toPlainText(), 0))

    def Conv_1_26B_AZ(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charDecode(self.editor.toPlainText(), 1, False, True))

    def Conv_0_25B_AZ(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charDecode(self.editor.toPlainText(), 0, False, True))

    def ASCIIText(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charDecode(self.editor.toPlainText(), 0, True, False))

    def ASCIIBText(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.charDecode(self.editor.toPlainText(), 0, True, True))

    def Convert_10_2(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 10, 2))

    def Convert_10_8(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 10, 8))

    def Convert_10_16(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 10, 16))

    def Convert_2_10(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 2, 10))

    def Convert_2_8(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 2, 8))

    def Convert_2_16(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 2, 16))

    def Convert_8_2(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 8, 2))

    def Convert_8_10(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 8, 10))

    def Convert_8_16(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 8, 16))

    def Convert_16_2(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 16, 2))

    def Convert_16_8(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 16, 8))

    def Convert_16_10(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertBaseGenString(self.editor.toPlainText(), 16, 10))

    def ConvertTabSpace1(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.tabsToSpaces(self.editor.toPlainText(), 1))

    def ConvertTabSpace2(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.tabsToSpaces(self.editor.toPlainText(), 2))

    def ConvertTabSpace3(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.tabsToSpaces(self.editor.toPlainText(), 3))

    def ConvertTabSpace4(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.tabsToSpaces(self.editor.toPlainText(), 4))

    def ConvertTabSpace5(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.tabsToSpaces(self.editor.toPlainText(), 5))

    def ConvertSpaceTab(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.SpacesToTabs(self.editor.toPlainText()))

    def tabsToSpaces(self, istr, numspaces):
        """ Converts all the tabs in istr to numspaces spaces. """
        spacestr = ""
        for i in range(numspaces):
            spacestr += ' '
        return istr.replace('\t', spacestr)

    def SpacesToTabs(self, istr):
        """ Intermediate menu call function. """
        return istr.replace(' ', '\t')

    def RemoveComments(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.RemoveCJCommentsFromString(self.editor.toPlainText()))

    def RemoveCJCommentsFromString(self, istr):
        """ Removes all C++/Java style comments from the string. """
        linelist = istr.split('\n')
        retstr = ""

        for line in linelist:
            try:
                pos = line.index("//")
                line = line[:pos]
            except:
                pass

            retstr += line + "\n"

        multilinecomment = True
        while multilinecomment:
            try:
                pos = retstr.index("/*")
                endpos = retstr.index("*/", pos)
                retstr = retstr[:pos] + retstr[endpos + 2:]
            except:
                multilinecomment = False

        return retstr

    def ConvertToCodeString(self):
        """ Intermediate menu call function. """
        self.updateEditor(self.ConvertToCPPCodeString(self.editor.toPlainText()))

    def ConvertToCPPCodeString(self, istr):
        """ Converts istr to a C++ style string per line with newline characters at the end.  """
        linelist = istr.split('\n')
        retstr = ""

        for line in linelist:
            retstr += "\"" + line + "\\n\"\n"

        return retstr

    def Condense(self):
        """ Does multiple transformations on the string, removes comments, trims lines, and removes blank lines. """
        istr = self.editor.toPlainText()
        istr = self.RemoveCJCommentsFromString(istr)
        istr = self.trimLines(istr, False, True)
        istr = self.removeBlankLines(istr)
        self.updateEditor(istr)

    def CondenseConvert(self):
        """
        Does multiple transformations on the string, removes comments, trims lines, removes blank lines, and converts to a code string.
        """
        istr = self.editor.toPlainText()
        istr = self.RemoveCJCommentsFromString(istr)
        istr = self.trimLines(istr, False, True)
        istr = self.removeBlankLines(istr)
        istr = self.ConvertToCPPCodeString(istr)
        self.updateEditor(istr)

    def RandIntRange(self):
        """ Random number generator: Uniform Integer """
        dialog = UniformRandIntDialog(self)

        if dialog.exec():
            try:
                seedStr = dialog.getSeed()
                lowerStr = dialog.getLowerBound()
                upperStr = dialog.getUpperBound()

                if seedStr.strip() == "":
                    seedVal = -1
                else:
                    seedVal = int(seedStr)

                if lowerStr.strip() == "":
                    lower = 0
                else:
                    lower = int(lowerStr)

                if upperStr.strip() == "":
                    upper = 0
                else:
                    upper = int(upperStr)

                if lower > upper:
                    temp = lower
                    lower = upper
                    upper = temp

                if seedVal >= 0:
                    seed(seedVal)

                numNums = dialog.getNumber()
                retstr = ""
                for i in range(numNums):
                    retstr += str(randint(lower, upper)) + "\n"
                self.updateEditor(retstr)
            except:
                QMessageBox.warning(self,"Error","There was an error in the input values.", QMessageBox.Ok)

    def RandFloatRange(self):
        """ Random number generator: Uniform Float """
        dialog = UniformRandIntDialog(self, "Uniform Random Float Generator", 200, False)

        if dialog.exec():
            try:
                seedStr = dialog.getSeed()
                lowerStr = dialog.getLowerBound()
                upperStr = dialog.getUpperBound()

                if seedStr.strip() == "":
                    seedVal = -1
                else:
                    seedVal = int(seedStr)

                if lowerStr.strip() == "":
                    lower = 0.0
                else:
                    lower = float(lowerStr)

                if upperStr.strip() == "":
                    upper = 0.0
                else:
                    upper = float(upperStr)

                if lower > upper:
                    temp = lower
                    lower = upper
                    upper = temp

                if seedVal >= 0:
                    seed(seedVal)

                numNums = dialog.getNumber()
                retstr = ""
                for i in range(numNums):
                    retstr += str(uniform(lower, upper)) + "\n"
                self.updateEditor(retstr)
            except:
                QMessageBox.warning(self,"Error","There was an error in the input values.", QMessageBox.Ok)

    def RandBinomial(self):
        """ Random number generator: Binomial """
        dialog = BinomailRandDialog(self)

        if dialog.exec():
            seedStr = dialog.getSeed()
            numNums = dialog.getNumber()
            trials = dialog.getTrials()
            prob = dialog.getProb()

            if seedStr.strip() == "":
                seedVal = -1
            else:
                seedVal = int(seedStr)

            if seedVal >= 0:
                seed(seedVal)

            retstr = ""
            for i in range(numNums):
                val = sum(random.uniform(0, 1) < prob for i in range(trials))
                retstr += str(val) + "\n"

            self.updateEditor(retstr)

    def RandNormal(self):
        """ Random number generator: Normal """
        dialog = NormalRandDialog(self)

        if dialog.exec():
            seedStr = dialog.getSeed()
            numNums = dialog.getNumber()
            mu = dialog.getMu()
            sigma = dialog.getSigma()

            if seedStr.strip() == "":
                seedVal = -1
            else:
                seedVal = int(seedStr)

            if seedVal >= 0:
                seed(seedVal)

            retstr = ""
            for i in range(numNums):
                retstr += str(normalvariate(mu, sigma)) + "\n"

            self.updateEditor(retstr)

    def RandLogNormal(self):
        """ Random number generator: Log Normal """
        dialog = NormalRandDialog(self, True)

        if dialog.exec():
            seedStr = dialog.getSeed()
            numNums = dialog.getNumber()
            mu = dialog.getMu()
            sigma = dialog.getSigma()

            if seedStr.strip() == "":
                seedVal = -1
            else:
                seedVal = int(seedStr)

            if seedVal >= 0:
                seed(seedVal)

            retstr = ""
            for i in range(numNums):
                retstr += str(lognormvariate(mu, sigma)) + "\n"

            self.updateEditor(retstr)

    def RandExp(self):
        """ Random number generator: Exponential """
        dialog = ExpRandDialog(self)

        if dialog.exec():
            seedStr = dialog.getSeed()
            numNums = dialog.getNumber()
            lamb = dialog.getLambda()

            if seedStr.strip() == "":
                seedVal = -1
            else:
                seedVal = int(seedStr)

            if seedVal >= 0:
                seed(seedVal)

            retstr = ""
            for i in range(numNums):
                retstr += str(expovariate(lamb)) + "\n"

            self.updateEditor(retstr)


    def RandBBS(self):
        """ Random bit generator: Blum-Blum-Shub """
        dialog = BBSRandBitDialog(self)

        if dialog.exec():
            seedStr = dialog.getSeed()
            PStr = dialog.getP()
            QStr = dialog.getQ()
            numNums = dialog.getNumber()
            bitlangth = dialog.getBitLength()
            seed = int(seedStr)
            p = int(PStr)
            q = int(QStr)
            n = p*q
            x = seed**2 % n
            retstr = ""
            for i in range(numNums):
                numstr = ""
                for j in range(bitlangth):
                    x = x ** 2 % n
                    bit = x % 2
                    numstr += str(bit)

                retstr += numstr + "\n"

            self.updateEditor(retstr)
