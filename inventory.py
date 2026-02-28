"""
File: inventory.py
Description: 
"""

from computer import Linux, Windows
# from linked import LinkedComputer named your file this.


def printMenu():
    print("MENU")
    print("L List all computers in your inventory")
    print("A Add a computer")
    print("R Remove some computers")
    print("Q Quit")


def readInt(prompt):
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            return int(s)
        print("No match. Please enter a whole number.\n")


def readGB(prompt):
    # accepts: "500", "500GB", "500 GB"
    while True:
        s = input(prompt).strip().lower().replace(" ", "")
        if s.endswith("gb"):
            s = s[:-2]
        if s.isdigit():
            gb = int(s)
            if gb > 0:
                return gb
        print("No match. Enter a positive number like 500 GB.\n")

def main():
    pass
