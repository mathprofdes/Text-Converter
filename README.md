# Text Converter

**Download the Current Version (1.3.1)**

**Windows Users**

This is a Python application using the PySide6 GUI API, but you do not need to have either Python nor PySide6 installed on your machine to run this program. The Windows distribution of this program is as a single stand-alone executable file, TextConverter.exe.  This software has been tested on both Windows 10 and 11.

- Download the **[TextConverter.exe](https://github.com/mathprofdes/Text-Converter/releases/download/v1.3.1/TextConverter.exe)** file.
- From Windows Explorer double-click the TextConverter.exe file.


**MacOS (Silicon) Users**

This is a Python application, but you do not need to have either Python nor its dependency packages installed on your machine to run this program. The MacOS distribution of this program is a MacOS application for the M series Macs.  The software has been compiled and tested on a Mac M3 running Tahoe.

- Download the **[TextConverter.zip](https://github.com/mathprofdes/Text-Converter/releases/download/v1.3.1/TextConverter.zip)** file.  Safari should automatically unzip the application.  
  - Note: Alternatively, you can download the **[TextConverter.app.tar.gz](https://github.com/mathprofdes/Text-Converter/releases/download/v1.3.1/TextConverter.app.tar.gz)** file, and using Finder, extract the application from it.
- In Finder double-click the TextConverter application.  If you get a warning that the file cannot be run you can do the following.
  - Open the System Settings.
  - Click Privacy & Security on the side list.
  - Scroll down to the  security section.
  - Click Open Anyway.
  - Type in your password to confirm.
- You can run the program from any folder on the machine or drag it into your Applications folder and run it from there. 

**Linux Users**

This is a Python application using the PySide6 and several other packages. The easiest way to run this program is either from the source code using PyCharm or to create an executable file for your system. Please see the instructions below.

--- 

**Running the Program in PyCharm**

- Download and extract the Source Code file from the most current release. 
- Create a new PyCharm project named TextConverter, use a virtual environment.
- Copy all the files and directories from the source code directory over to the project in PyCharm.
- From the PyCharm package manager install the PySide6 (6.10.0) package.
- Run the program.

**Create an Executable for Your System**

To create an executable for your system, make the PyCharm project as above. Then, 

- From the PyCharm package manager install pyinstaller.
- In the terminal in PyCharm, run ``pyinstaller -F --windowed TextConverter.py``.  This will create a TextConverter.spec file.
- Open the TextConverter.spec file in PyCharm and change the datas line to ``datas=[('Help','Help')],``
- In the terminal in PyCharm, run ``pyinstaller TextConverter.spec``.
- A ``dist`` directory will have been created and in it is a single file ``TextConverter`` that is an executable for your system.
- Copy this executable to where you want to store it and you can run it like any other program on your system. 

---


**Notes:** 
- For Linux and MacOS users, depending on how your system is set up, you may be able to simply double-click the TextConverter.py file from your file browser instead of running this from the terminal.
- A png file of a program icon **[ProgramIcon.png](https://github.com/mathprofdes/Text-Converter/releases/download/v1.3.1/ProgramIcon.png)** is included if you wish to use it for a shortcut to the program.

---

**Program Description**

The Text Converter is a simple text and numeric manipulation application that allows the user to do some specialized conversions that may not be available in a standard text editor or programming IDE.

---

**Updates**

- Added line numbering and current line highlighting.
- Changed options from converting the text of the entire document to converting the text of the selection.  So to do a conversion, select the desired text and then select the conversion from the menu.

---

**Screenshot**

![Screenshot of program.](https://github.com/mathprofdes/Text-Converter/releases/download/v1.3.1/TextConverterScreenshot.png)
