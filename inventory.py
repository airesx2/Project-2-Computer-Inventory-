"""
File: inventory.py
Description: 
Consists of the main program, processing user input and instatiates appropriate objs which are added to the linked structure
"""
from computer import Linux, Windows
from linked import LinkedComputer


def printMenu():
    #TODO
    """_summary_
    """
    print("MENU")
    print("L List all computers in your inventory\n")
    print("A Add a computer")
    print("R Remove some computers\n")
    print("Q Quit")


def readInt(prompt):
    #TODO
    """_summary_

    Args:
        prompt (_type_): _description_

    Returns:
        _type_: _description_
    """
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            return int(s)
        print("No match. Please enter a whole number.\n")


def readGB(prompt):
    #TODO
    """_summary_

    Args:
        prompt (_type_): _description_

    Returns:
        _type_: _description_
    """
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
    #TODO
    """_summary_

    Args:
        ip (_type_): _description_

    Returns:
        _type_: _description_
    """
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
    #TODO
    """_summary_

    Returns:
        _type_: _description_
    """
    while True:
        ip = input("Enter the computer’s IP address: ").strip()
        if validIP(ip):
            return ip
        print("No match. Invalid IP address.\n")


def printTable(comps):
    #TODO
    """_summary_

    Args:
        comps (_type_): _description_
    """
    print("Year purchased  IP address       Storage space           Operating system")
    print("-" * 74)
    current = comps.head
    while current:
        year = current.data.yearPurchased
        ip = current.data.ip
        space = current.data.getStorageText()
        os = current.data.os
        print(f"{year:<15} {ip:<15} {space:<24} {os}")
        current = current.next
    print()

def listComputers(inv):
    #TODO
    """_summary_

    Args:
        inv (_type_): _description_
    """

    if inv.len() == 0:
        print("No match. There are no computers in the inventory.\n")
        return
    printTable(inv)
    print("\n\n")

def addComputer(inv):
    #TODO
    """_summary_

    Args:
        inv (_type_): _description_

    Returns:
        _type_: _description_
    """
    ip = readIP()
    year = input("Enter the year purchase: ")
    os = input("Enter the operating system: ")
    if "windows" in os.lower():
        space = input("Enter the C drive capacity: ")
        inst = Windows(ip, year, os, space)
        print("\n\n")
    elif "linux" in os.lower():
        space = input("Enter the file system capacity: ")
        inst = Linux(ip, year, os, space)
        print("\n\n")
    else:
        print("\nNo match. Please provide a valid os option.\n")
        return
    
    return inst
    
    
def removeComputers(inv):
    #TODO
    """_summary_

    Args:
        inv (_type_): _description_
    """
    rm = int(input("How many computers do you want to remove: "))
    if rm > inv.len():
        print("You are removing more than you have.")
        return
    
    removedComps = LinkedComputer()

    while rm != 0:
        c = inv.remove()
        removedComps.add(c)
        rm -= 1
    print("\nYou have removed the following computer: \n")
    printTable(removedComps)


def start():
    #TODO
    """_summary_
    """
    inv = LinkedComputer()

    while True:
        printMenu()
        choice = input("...your choice: ").strip().lower()
        print()
        if choice == "l":
            listComputers(inv)
        elif choice == "a":
            newComp = addComputer(inv) 
            inv.add(newComp)
        elif choice == "r":
            removeComputers(inv) # We need to complete this
        elif choice == "q":
            print("Thanks for using my program! :)")
            break
        else:
            print("No match.\n")


if __name__ == "__main__":
    start()

