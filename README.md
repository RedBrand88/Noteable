# Noteable
Automated note taking app for the terminal. It leverages vim but it could leverage any text editor.

This has not been tested on windows cmd prompt

## Install

1. clone the repository
1. cd into the Noteable directory
1. run ```python installNotable.py```
1. source your zshrc
1. run ```nhelp```
1. start taking notes!

## Commands

* nfe - args: note name (string), folder name (string), extenstion (string).
  * This command will create a file with the specified extension within the specified file. If ~/Documents/Notes does not exist that will be created and the specifed folder will be created within the Notes directory.
* nf - args: note name (string), folder name (string)
  * this command will create a text file within the specified folder
* no - args: full note name including extension (string)
  * this command will open an existing note with any directory inside the Note directory
* lf - args: none
  * this command will print a list of all directories and all the files within each directory to the console.
* dn - args: target file name with extension (string)
  * this command deletes a specified file if it exists within the Notes directory
* df - args: target folder name (string)
  * this command deletes a specified folder if the folder is empty
* nhelp - args: none
  * this command will list the available commands to the console