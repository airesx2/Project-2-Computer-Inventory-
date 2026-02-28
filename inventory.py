from computer import Linux, Windows
from linked import LinkedComputer


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
    while True:
        s = input(prompt).strip().lower().replace(" ", "")
        if s.endswith("gb"):
            s = s[:-2]
        if s.isdigit():
            gb = int(s)
            if gb > 0:
                return gb
        print("No match. Enter a positive number like 500 GB.\n")
def validIP(ip):
    parts = ip.strip().split(".")
    if len(parts) != 4:
        return False

    nums = []
    for p in parts:
        if p == "" or len(p) > 3:
            return False
        if not p.isdigit():
            return False
        n = int(p)
        if n < 0 or n > 255:
            return False
        nums.append(n)

    if nums == [0, 0, 0, 0]:
        return False

    return True


def readIP():
    while True:
        ip = input("Enter the computer’s IP address: ").strip()
        if validIP(ip):
            return ip
        print("No match. Invalid IP address.\n")


def printTable(comps):
    print("Year purchased  IP address       Storage space           Operating system")
    print("-" * 74)
    for c in comps:
        year = c.getYearPurchased()
        ip = c.ip
        space = c.getStorageText()
        os = c.os
        print(f"{year:<14} {ip:<15} {space:<22} {os}")
    print()

def listComputers(inv):
    if len(inv) == 0:
        print("No match. There are no computers in the inventory.\n")
        return
    printTable(inv.getAll())

def addComputer(inv):
    print("Finish")
    #We need to complete
def removeComputers(inv):
    print("Finish")
    #We need to complete
def start():
    inv = LinkedComputer()

    while True:
        printMenu()
        choice = input("...your choice: ").strip().lower()
        print()

        if choice == "l":
            listComputers(inv)
        elif choice == "a":
            addComputer(inv) # We need to complete this
        elif choice == "r":
            removeComputers(inv) # We need to complete this
        elif choice == "q":
            print("Thanks for using my program! :)")
            break
        else:
            print("No match.\n")


if __name__ == "__main__":
    start()
