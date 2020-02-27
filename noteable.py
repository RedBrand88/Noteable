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
        print(f"{root}")
        for file in files:
            print(f"    |{file}")

def openExistingFileinFolder(target):
    for root, dirs, files in os.walk(defaultRelativePath):
        if target in files:
            path = os.path.join(root, target)
            os.system("vim " + path)
        else:
            print(f"{target} does not exist in {root}")

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

def main():
    if sys.argv[1] == "nfe":
        createNoteFolderExtension()
    elif sys.argv[1] == "nf":
        createTextFileFolder()
    elif sys.argv[1] == "no":
       openExistingFileinFolder(sys.argv[2])
    elif sys.argv[1] == "lf":
        listExisitngFiles()

if __name__ == "__main__":
    main()

