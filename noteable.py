import sys
import os
from textfilecreator import textfilecreator

python = ".py"
js = ".js"
jsx = ".jsx"
text = ".txt"

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


def create():
    parentdirectory = "~/Documents/Notes/"
    extension = str(sys.argv[3])

    try:
        extension = extensions[extension]
    except Exception as e:
        print("failed to create file type " + str(e))
        extension = ".txt"

    filename = str(sys.argv[1]) + extension

    foldername = str(sys.argv[2])


    with textfilecreator(filename, foldername, parentdirectory):
        pass

    filepath = os.path.join(parentdirectory, foldername, filename)

    os.system("vim " + filepath)

if __name__ == "__main__":
    create()

