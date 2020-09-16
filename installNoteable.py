from datetime import date
from os import path

print("Downloading Noteable...")
with open(path.expanduser("~/.zshrc"), "at") as zshrc:
    zshrc.write(
        "\n"
        f"#Added by Noteable on {date.today()}\n"
        "nfe() {\n"
        "\tpython noteable.py nfe \"$1\" \"$2\" \"$3\"\n"
        "}\n"
        "nf() {\n"
        "\tpython noteable.py nf \"$1\" \"$2\"\n"
        "}\n"
        "no() {\n"
        "\tpython noteable.py no \"$1\"\n"
        "}\n"
        "lf() {\n"
        "\tpython noteable.py lf\n"
        "}\n"
        "dn() {\n"
        "\tpython noteable.py dn \"$1\"\n"
        "}\n"
        "df() {\n"
        "\tpython noteable.py df \"$1\"\n"
        "}\n"
        "nhelp() {\n"
        "\tpython noteable.py h\n"
        "}\n"
    )
    print("Finished Download\n")
    print("Run source command on your .zshrc file to activate new commands\n")
    print("ex. source ~/.zshrc")
    print("Happy note taking!")
