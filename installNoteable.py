from datetime import date
from os import path
import os
from textfilecreator import textfilecreator


def installZshCommands():
    executablePath = "~/Documents/Notes/Noteable/noteable.py"
    print("Downloading Noteable...")
    with open(path.expanduser("~/.zshrc"), "at") as zshrc:
        zshrc.write(
            "\n"
            f"#Added by Noteable on {date.today()}\n"
            "nfe() {\n"
            f"\tpython {executablePath} nfe \"$1\" \"$2\" \"$3\"\n"
            "}\n"
            "nf() {\n"
            f"\tpython {executablePath} nf \"$1\" \"$2\"\n"
            "}\n"
            "no() {\n"
            f"\tpython {executablePath} no \"$1\"\n"
            "}\n"
            "lf() {\n"
            f"\tpython {executablePath} lf\n"
            "}\n"
            "dn() {\n"
            f"\tpython {executablePath} dn \"$1\"\n"
            "}\n"
            "df() {\n"
            f"\tpython {executablePath} df \"$1\"\n"
            "}\n"
            "nhelp() {\n"
            f"\tpython {executablePath} h\n"
            "}\n"
        )
    print("Finished Download\n")
    print("Run source command on your .zshrc file to activate new commands\n")
    print("ex. source ~/.zshrc")
    print("Happy note taking!")


def copyFilesToAppFolder():
    defaultParentDirectory = "~/Documents/Notes/"
    directory = "Noteable"
    with textfilecreator("noteable.py", directory, defaultParentDirectory):
        pass
    print("Copying files to ~/Documents/Notes/Noteable...\n")
    os.system("cp noteable.py ~/Documents/Notes/Noteable/noteable.py")
    os.system("cp textfilecreator.py ~/Documents/Notes/Noteable/textfilecreator.py")
    print("finished copying\n")


def main():
    copyFilesToAppFolder()
    installZshCommands()

if __name__ == "__main__":
    main()
