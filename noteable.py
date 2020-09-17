import sys
import os
from textfilecreator import textfilecreator
import enum

python = ".py"
js = ".js"
jsx = ".jsx"
text = ".txt"
defualtextension = ".txt"
defaultparentdirectory = "~/Documents/Notes/"
defaultRelativePath = "../../../Documents/Notes"

extensions = {
    "py": python,
    ".py": python,
    "python": python,
    "js": js,
    ".js": js,
    "javascript": js,
    "jsx": jsx,
    ".jsx": jsx,
    "react": jsx,
    "text": text,
    ".txt": text,
    "txt": text,
}

class TextEditors(enum.Enum):
    Vim = "vim "

    def __str__(self):
        return f"{self.value}"


def findFile(target):
    for root, dirs, files in os.walk(os.path.expanduser(defaultparentdirectory)):
        if target in files:
            return os.path.join(root, target)
        elif target in dirs:
            return os.path.join(root, target)
    return None


def listExisitngFiles():
    for root, dirs, files in os.walk(os.path.expanduser(defaultparentdirectory)):
        dirString = root.split("/")[-1]
        if dirString == "Noteable" or dirString == "__pycache__":
            continue
        else:
            print(f"{dirString}")
            for file in files:
                print(f"    |{file}")


def openExistingFileinFolder(target):
    path = findFile(target)
    if path:
        os.system(str(TextEditors.Vim) + path)
    else:
        print(f"{target} does not exist in Notes")


def createTextFileFolder():
    parentdirectory = os.path.expanduser(defaultparentdirectory)
    filename = str(sys.argv[2]) + ".txt"
    foldername = str(sys.argv[3])

    with textfilecreator(filename, foldername, parentdirectory):
        pass

    filepath = os.path.join(parentdirectory, foldername, filename)

    os.system(str(TextEditors.Vim) + filepath)


def createNoteFolderExtension():
    parentdirectory = os.path.expanduser(defaultparentdirectory)
    try:
        extension = str(sys.argv[4])
    except IndexError:
        print("This command requires 3 inputs: filename, foldername, file extension")

    if extension is None:
        extension = "Undefined"
        print("failed to create file type " + extension)
        extension = defualtextension
    elif extension in extensions.keys():
        extension = extensions[extension]
    else:
        print("Failed to create file type " + extension)
        extension = defualtextension

    filename = str(sys.argv[2]) + extension

    foldername = str(sys.argv[3])

    with textfilecreator(filename, foldername, parentdirectory):
        pass

    filepath = os.path.join(parentdirectory, foldername, filename)

    os.system(str(TextEditors.Vim) + filepath)


def deleteNote(target):
    path = findFile(target)
    if path:
        response = input(f"Are you sure you want to delete {target}?: ")
        if response == 'y' or response == 'Y':
            os.remove(path)
            print(f"{target} deleted")
    else:
        print(f"{target} does not exist in Notes")

def deleteFolder(target):
    path = findFile(target)
    if path:
        response = input(f"You can only delete folders that are empty. Are you sure you want to delete {target}?: ")
        if response == 'y' or response == 'Y':
            os.rmdir(path)
            print(f"{target} deleted")
    else:
        print(f"{target} does not exist in Notes")


def noteableHelp():
    print("|--------------------------------------------------------------------|\n")
    print("|                         Noteable Commands                          |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|     Create note commands - commands that will create new notes     |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|  nfe - args: note name, folder name, extension                     |\n")
    print("|  nf - args: note name, folder name                                 |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|        Open note command - command that opens existing note        |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|  no - args: note name with extension                               |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|note list command - lists current notes and folders to the terminal |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|  lf - args: none                                                   |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|     Delete note command - commands that delete existing note       |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|  dn - args: note name with extension                               |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|  df - args: folder name                                            |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|  contribute @ https://github.com/RedBrand88/Noteable               |\n")
    print("|--------------------------------------------------------------------|")


def main():
    if sys.argv[1] == "nfe":
        createNoteFolderExtension()
    elif sys.argv[1] == "nf":
        createTextFileFolder()
    elif sys.argv[1] == "no":
        openExistingFileinFolder(sys.argv[2])
    elif sys.argv[1] == "lf":
        listExisitngFiles()
    elif sys.argv[1] == "dn":
        deleteNote(sys.argv[2])
    elif sys.argv[1] == "df":
        deleteFolder(sys.argv[2])
    elif sys.argv[1] == "h":
        noteableHelp()


if __name__ == "__main__":
    main()
