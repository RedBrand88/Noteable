import sys
import os
from textfilecreator import textfilecreator

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


def listExisitngFiles():
    for root, dirs, files in os.walk(defaultRelativePath):
        dirString = root.split("/")[-1]
        print(f"{dirString}")
        for file in files:
            print(f"    |{file}")


def openExistingFileinFolder(target):
    found = False
    for root, dirs, files in os.walk(defaultRelativePath):
        if target in files:
            found = True
            path = os.path.join(root, target)
            os.system("vim " + path)

    if not found:
        print(f"{target} does not exist in Notes")


def createTextFileFolder():
    parentdirectory = defaultparentdirectory
    filename = str(sys.argv[2]) + ".txt"
    foldername = str(sys.argv[3])

    with textfilecreator(filename, foldername, parentdirectory):
        pass

    filepath = os.path.join(parentdirectory, foldername, filename)

    os.system("vim " + filepath)


def createNoteFolderExtension():
    parentdirectory = defaultparentdirectory
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

    os.system("vim " + filepath)


def noteableHelp():
    print("|--------------------------------------------------------------------|\n")
    print("|                         Noteable Commands                          |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|     Create note commands - commands that will create new notes     |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|  nfe - args: note name, folder name, extension                     |\n")
    print("|  ng - args: note name, folder name, extension will be .txt         |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|        Open note command - command that opens existing note        |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|  no - args: note name with extension                               |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|note list command - lists current notes and folders to the terminal |\n")
    print("|--------------------------------------------------------------------|\n")
    print("|  lf - args: none                                                   |\n")
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
    elif sys.argv[1] == "noteable -h":
        noteableHelp()


if __name__ == "__main__":
    main()
