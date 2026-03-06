"""
File: inventory.py

Description:
    Contains the main program logic for managing a computer inventory.
    It processes user input, creates the appropriate computer objects,
    and stores them in a linked structure.
"""

from computer import Linux, Windows
from linked import LinkedComputer


def printMenu():
    """
    Display the main menu options for the inventory program.
    """
    print("MENU")
    print("L List all computers in your inventory\n")
    print("A Add a computer")
    print("R Remove some computers\n")
    print("Q Quit")


def readInt(prompt):
    """
    Prompt the user to enter a whole number and keep asking until valid input is given.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        int: A valid whole number entered by the user.
    """
    while True:
        s = input(prompt).strip()
        #input is valid if it's a whole number (no decimals, no negative sign)
        if s.isdigit():
            return int(s)
        print("No match. Please enter a whole number.\n")


def readGB(prompt):
    """
    Prompt the user to enter a positive storage size in gigabytes.

    The user may enter a value such as '500' or '500 GB'. The function
    removes spaces and ignores letter case before validating the input.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        int: A positive integer representing storage size in gigabytes.
    """
    #input is valid if it is a positive number with optional "GB" suffix (ignore spaces and case)
    while True:
        s = input(prompt).strip().lower().replace(" ", "")
        #check if the input ends with "gb", remove before validating the number
        if s.endswith("gb"):
            s = s[:-2]
        #check if the remaining string is a positive whole number
        if s.isdigit():
            gb = int(s)
            #check if the number is greater than 0
            if gb > 0:
                return gb
        print("No match. Enter a positive number like 500 GB.\n")


def validIP(ip):
    """
    Check whether a string is a valid IPv4 address.

    A valid IP address must:
    - Contain exactly four parts separated by periods
    - Have only numeric parts
    - Have each part between 0 and 255
    - Not be 0.0.0.0

    Args:
        ip (str): The IP address string to validate.

    Returns:
        bool: True if the IP address is valid, otherwise False.
    """
    parts = ip.strip().split(".")
    #check if there are exactly 4 parts separated by periods
    if len(parts) != 4:
        return False

    nums = []
    #validate each part of the IP address according to the rules outlined above
    for p in parts:
        #check if part is empty, has more than 3 characters
        if p == "" or len(p) > 3:
            return False
        #check if part is not numeric
        if not p.isdigit():
            return False
        n = int(p)
        #check if part is outside the valid range of 0-255
        if n < 0 or n > 255:
            return False
        nums.append(n)

    #check if all parts are zero 
    if nums == [0, 0, 0, 0]:
        return False

    return True


def readIP():
    """
    Prompt the user to enter a valid IPv4 address.

    Keeps asking until the user provides an IP address that passes validation.

    Returns:
        str: A valid IPv4 address entered by the user.
    """
    #input is valid if it has 4 numeric parts separated by periods, each part between 0-255, and not all zeros
    while True:
        ip = input("Enter the computer’s IP address: ").strip()
        #check if the input is a valid IP address (validIP function)
        if validIP(ip):
            return ip
        print("No match. Invalid IP address.\n")


def printTable(comps):
    """
    Print all computers in a formatted table.

    Args:
        comps (LinkedComputer): A linked structure containing computer objects to display.
    """
    print("Year purchased  IP address       Storage space           Operating system")
    print("-" * 74)
    current = comps.head
    #traverse the linked list and print each computer's details
    while current:
        year = current.data.yearPurchased
        ip = current.data.ip
        space = current.data.getStorageText() + " GB"
        os = current.data.os
        print(f"{year:<15} {ip:<15} {space:<24} {os}")
        current = current.next
    print()


def listComputers(inv):
    """
    Display all computers currently in the inventory.

    If the inventory is empty, an appropriate message is shown.

    Args:
        inv (LinkedComputer): The inventory containing computer objects.
    """
    #check if the inventory is empty 
    if inv.len() == 0:
        print("No match. There are no computers in the inventory.\n")
        return
    printTable(inv)
    print("\n\n")


def addComputer(inv):
    """
    Prompt the user for computer details and create a new computer object.

    If the operating system contains 'windows', a Windows object is created.
    If the operating system contains 'linux', a Linux object is created.
    If the operating system is invalid, no object is created.

    Args:
        inv (LinkedComputer): The inventory where the computer may later be added.

    Returns:
        Windows | Linux | None: The created computer object, or None if the OS is invalid.
    """
    ip = readIP()
    year = readInt("Enter the year purchased: ")
    os = input("Enter the operating system: ")
    #check if inputted os is windows
    if "windows" in os.lower():
        space = readGB("Enter the C drive capacity: ")
        inst = Windows(ip, year, os, space)
        print("\n\n")
    #check if inputted os is linux
    elif "linux" in os.lower():
        space = readGB("Enter the file system capacity: ")
        inst = Linux(ip, year, os, space)
        print("\n\n")
    else:
        print("\nNo match. Please provide a valid os option.\n")
        return
    
    return inst
    
    
def removeComputers(inv):
    """
    Remove a specified number of computers from the inventory.

    Removed computers are stored temporarily in a separate linked structure
    and then displayed to the user.

    Args:
        inv (LinkedComputer): The inventory from which computers will be removed.
    """
    rm = readInt("How many computers do you want to remove: ")
    #check if the user is trying to remove more computers than are in the inventory
    if rm > inv.len():
        print("You are removing more than you have.")
        return
    
    removedComps = LinkedComputer()

    #remove the specified no. of computers from inventory and add them to removedComps linked list
    while rm != 0:
        c = inv.remove()
        removedComps.add(c)
        rm -= 1
    print("\nYou have removed the following computer: \n")
    printTable(removedComps)


def start():
    """
    Start the inventory program and process user menu selections.

    Creates an empty inventory and continues running until the user chooses to quit.
    """
    inv = LinkedComputer()

    #prints user menu and processes user input until they choose to quit
    while True:
        printMenu()
        choice = input("...your choice: ").strip().lower()
        print()
        #list computers
        if choice == "l":
            listComputers(inv)
        #add computers
        elif choice == "a":
            newComp = addComputer(inv) 
            #avoid None objects being added to the inventory 
            if newComp is not None:
                inv.add(newComp)
        #remove computers
        elif choice == "r":
            removeComputers(inv) 
        #quit program
        elif choice == "q":
            print("Thanks for using my program! :)")
            break
        else:
            print("No match.\n")

#start the program
if __name__ == "__main__":
    start()
