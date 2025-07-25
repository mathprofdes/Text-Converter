Editing Options
===============

File Menu
---------

* **New**: Clears the editing area.  The text that is currently in the editing area is stored in the undo/redo history and hence can be retrieved with an undo.

* **Open/Insert**: Opens an Open dialog box for loading a text file into the editing area.  The loaded file is inserted at the current cursor position and any text in the editing area is not removed. As with the New option, the current text is stored in the undo/redo history and hence can be retrieved with an undo.

* **Save as**: Opens a Save as dialog box for saving the current document to a text file. Note that there is not a straight Save option. This was intentional in the design, we did not want the program to make it easy to overwrite a loaded file.

* **Print**: Opens a Print dialog box for printing the current document to the selected printer.

* **Print Preview**: Opens a Print Preview dialog box for viewing the printed page layout, option changes and can invoke the printing of the current document to the selected printer.

* **Statistics**: Displays a small dialog box with the character, non-space character, and word counts.

* **Open a New Editor Window**: Opens a new copy of the Text Editor & Converter application.

* **Exit**: Closes the program. There is no exit catch if there is an unsaved edit.


Edit Menu
---------

* **Cut**: Removes selected text and copies it to the system clipboard.

* **Copy**: Copies selected text to the system clipboard.

* **Copy All**: Copies the entire document to the system clipboard.

* **Paste**: Pastes current clipboard text into the editor at the current cursor position.

* **Select All**: Selects all text in the editor.

* **Undo**: Undoes the last change in the editor.

* **Redo**: Redoes the last undo.

* **Toggle Word Wrap**: Toggles the editor's word wrap state.


Strings Menu
------------

* **UPPERCASE**: Converts the entire editor text to uppercase.

* **lowercase**: Converts the entire editor text to lowercase.

* **Capitalize**: Capitalizes each word in the editor.

* **Remove All Whitespace**: Removes all whitespace characters from the editor text, including whitespace between non-whitespace characters.

* **Whitespace to Single Spaces**: Replaces all whitespace character sequences with a single space character.

* **Remove Whitespace Per Line**: Removes all whitespace characters from the editor text, including whitespace between non-whitespace characters line by line.

* **Remove Punctuation**: Removes all punctuation characters from the editor text.

* **Remove Numbers**: Removes all numeric characters from the editor text.

* **Remove All Non-Letters**: Removes all characters that are not alphabetic characters.

* **Split (Spaces to Line Breaks)**: Converts all spaces to line breaks.

* **Join (Line Breaks to Spaces)**: Converts all line breaks to spaces.

* **Remove Blank Lines**: Removes all blank lines from the editor text.

* **Remove Multiple Blank Lines**: Converts multiple blank lines to a single blank line.

* **Remove Front Whitespace**: Removes whitespace characters from the beginning of each line. Any whitespace characters at the end of the line or between non-whitespace characters are not removed.

* **Remove End Whitespace**: Removes whitespace characters from the end of each line. Any whitespace characters at the beginning of the line or between non-whitespace characters are not removed.

* **Trim Lines**: Removes whitespace characters from the beginning and end of each line. Any whitespace characters between non-whitespace characters are not removed.

* **Convert Tabs to Spaces**: Replaces all tab characters with the desired (selected in the submenu) number of spaces (1-5).

* **Convert Spaces to Tabs**: Replaces all space characters with a tab character.

* **Replace All**: Brings up a dialog box allowing the user to input target and replacement strings and will replace all occurrences of the target with the replacement. The replacement is done in a case sensitive manner.

* **Split At**: Brings up a dialog box allowing the user to input a string that will be used for splitting the editor text. The string that is split over is removed from the text and replaced with line breaks.

* **Break Character Stream**: Brings up a dialog box allowing the user to select the number of characters for each line and places a line break after each block of characters of this length. There is also an option for preserving words that will put the break after the word the fills the block. So in if this option is selected there may be lines longer than the block size selected.

* **Reformat Text**: Brings up a dialog box allowing the user to select the maximum number of characters for each line and places a line break after each block of characters of this length. This automatically preserves words when possible.



Characters Menu
---------------

* **A-Z -> 1-26**: Codes characters A-Z as 1-26. Lowercase characters are converted to uppercase before coding and all other characters are ignored. For example, ``abcde, fgh`` is coded as ``1 2 3 4 5 6 7 8``.

* **A-Z -> 01-26**: Codes characters A-Z as 01-26. Lowercase characters are converted to uppercase before coding and all other characters are ignored. For example, ``abcde, fgh`` is coded as ``01 02 03 04 05 06 07 08``.

* **A-Z -> 0-25**: Codes characters A-Z as 1-26. Lowercase characters are converted to uppercase before coding and all other characters are ignored. For example, ``abcde, fgh`` is coded as ``0 1 2 3 4 5 6 7``.

* **A-Z -> 00-25**: Codes characters A-Z as 01-26. Lowercase characters are converted to uppercase before coding and all other characters are ignored. For example, ``abcde, fgh`` is coded as ``00 01 02 03 04 05 06 07``.

* **A-Z -> 1-26 Binary**: Codes characters A-Z as 1-26 and output is in binary form. Lowercase characters are converted to uppercase before coding and all other characters are ignored. For example, ``abcde, fgh`` is coded as ``1 10 11 100 101 110 111 1000``.

* **A-Z -> 0-25 Binary**: Codes characters A-Z as 0-25 and output is in binary form. Lowercase characters are converted to uppercase before coding and all other characters are ignored. For example, ``abcde, fgh`` is coded as ``0 1 10 11 100 101 110 111``.

* **A-Z -> 1-26 8-Bit Binary**: Codes characters A-Z as 1-26 and output is in 8-bit binary form. Lowercase characters are converted to uppercase before coding and all other characters are ignored. For example, ``abcde, fgh`` is coded as ``00000001 00000010 00000011 00000100 00000101 00000110 00000111 00001000``.

* **A-Z -> 0-25 8-Bit Binary**: Codes characters A-Z as 0-25 and output is in 8-bit binary form. Lowercase characters are converted to uppercase before coding and all other characters are ignored. For example, ``abcde, fgh`` is coded as ``00000000 00000001 00000010 00000011 00000100 00000101 00000110 00000111``.

* **Text -> ASCII**: Codes each character to its ASCII value. The input is assumed to be keyboard characters within the ASCII table.

* **Text -> ASCII: 3 Digits**: Codes each character to its ASCII value using 3 digits for each number, padding the beginning with zeros if needed.

* **Text -> ASCII: Binary**: Codes each character to its ASCII value and returns the binary representation of the number.

* **Text -> ASCII: 8-Bit Binary**: Codes each character to its ASCII value and returns the 8-Bit binary representation of the number.

* **1-26 -> A-Z**: Converts the 1-26 numeric coding back to A-Z.

* **0-25 -> A-Z**: Converts the 0-25 numeric coding back to A-Z.

* **1-26 Binary -> A-Z**: Converts the binary 1-26 numeric coding back to A-Z.

* **0-25 Binary -> A-Z**: Converts the binary 0-25 numeric coding back to A-Z.

* **ASCII -> Text**: Converts the ASCII value coding back to text. It assumes that each number is between 0 and 255.

* **ASCII Binary -> Text**: Converts the binary ASCII value coding back to text. It assumes that each number is between 0 and 255.


Numbers Menu
------------

* **Decimal -> Binary**: Converts decimal numbers to binary.

* **Decimal -> Octal**: Converts decimal numbers to octal.

* **Decimal -> Hexadecimal**: Converts decimal numbers to hexadecimal.

* **Binary -> Decimal**: Converts binary numbers to decimal.

* **Binary -> Octal**: Converts binary numbers to octal.

* **Binary -> Hexadecimal**: Converts binary numbers to hexadecimal.

* **Octal -> Decimal**: Converts octal numbers to decimal.

* **Octal -> Binary**: Converts octal numbers to binary.

* **Octal -> Hexadecimal**: Converts octal numbers to hexadecimal.

* **Hexadecimal -> Decimal**: Converts hexadecimal numbers to decimal.

* **Hexadecimal -> Binary**: Converts hexadecimal numbers to binary.

* **Hexadecimal -> Octal**: Converts hexadecimal numbers to octal.

* **General Base Conversion...**: Allows the user to select the base conversion by inputting the original and target bases. Bases are restricted to be between 2 and 36, as with hexadecimal representation the a, b, c, d, e, f, sequence is continued with g, h, i, ... for bases that exceed 16.

* **Remove Leading Zeros**: Removes leading zeros from numbers.

* **Remove Leading Zeros with Minimum Length...**: Removes leading zeros from numbers but allows the user to select a minimum length of the resulting number. For example, with the value 00001101, if the user selects a minimum length of 5 the result will be 01101.

* **Pad with Zeros...**: Pads the beginning of each number with zeros up to a maximum length that is specified by the user. For example, if the number is 42 and the user selects a length of 5 the result will be 00042. Likewise, if the user selects a length of 2 (or 0 or 1) the result will be 42.


Random Menu
-----------

* **Uniform Integer Range...**: This will produce a list of pseudo-random integers, between a user-selected lower bound and upper bound, inclusive. Numbers are generated using Python's built-in random number generator. A dialog box will open allowing the user to select the number of numbers to produce, the seed (starting point) of the generator, and the lower and upper bounds for the output. The seed option has a button that will allow the user to use the current time from the system clock. The output is a list of pseudo-random numbers in the specified range.

* **Uniform Float Range...**: This will produce a list of pseudo-random floats, between a user-selected lower bound and upper bound, inclusive. Numbers are generated using Python's built-in random number generator. A dialog box will open allowing the user to select the number of numbers to produce, the seed (starting point) of the generator, and the lower and upper bounds for the output. The seed option has a button that will allow the user to use the current time from the system clock. The output is a list of pseudo-random numbers in the specified range.

* **Binomial Distribution...**: This will produce a list of pseudo-random integers from a binomial distribution. A dialog box will open allowing the user to select the number of numbers to produce, the seed (starting point) of the generator, the number of trials for each value and the probability of a success. The seed option has a button that will allow the user to use the current time from the system clock. The output is the number of successes for each trial run.

* **Normal Distribution...**: This will produce a list of pseudo-random floats from a normal distribution. A dialog box will open allowing the user to select the number of numbers to produce, the seed (starting point) of the generator, mu and sigma. The seed option has a button that will allow the user to use the current time from the system clock.

* **Log Normal Distribution...**: This will produce a list of pseudo-random floats from a log normal distribution. A dialog box will open allowing the user to select the number of numbers to produce, the seed (starting point) of the generator, mu and sigma. The seed option has a button that will allow the user to use the current time from the system clock.

* **Exponential Distribution...**: This will produce a list of pseudo-random floats from an exponential distribution. A dialog box will open allowing the user to select the number of numbers to produce, the seed (starting point) of the generator, and lambda. The seed option has a button that will allow the user to use the current time from the system clock.

* **Blum-Blum-Shub Bit Generator...**: This will produce a list of random bit sequences using the Blum-Blum-Shub (BBS) algorithm. A dialog box will open allowing the user to select the number of numbers to produce, the length of each bit sequence, the seed (starting point) of the generator, and the two primes p and q. The seed option has a button that will allow the user to use a random seed that is relatively prime to p*q. In the BBS algorithm the modulus for the system is the product of two large primes p and q that are both congruent to 3 mod 4. The inputs for p and q each have is prime and next prime buttons that will check if the input value is prime and congruent to 3 mod 4 or find the next prime congruent to 3 mod 4. The output is a list of pseudo-random bit sequences of the user specified length.


Code Menu
---------

* **Remove C++/Java Style Comments**: Removes standard single line `//` and multi-line `/* */` comments from the code.

* **Convert to C++ Code String**: Converts each line to a C++ style string that can be directly assigned to a string variable.

* **Condense**: Removes comments, blank lines, and ending whitespace.

* **Condense & Convert to C++ Code String**: Removes comments, blank lines, and ending whitespace, then converts each line to a C++ style string.

