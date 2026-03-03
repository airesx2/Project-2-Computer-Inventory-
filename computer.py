"""
File: computer.py
Authors: Taran M, Arieana L 
Assignment: Project 2: Computer Inventory Using Linked Structure and Inheritance
Created: 02/26/2026
Description: 
Creation of classes ComputerSystem, Linux, Windows with appropriate inheritance and methods for each. 
"""


class ComputerSystem:
    """
    ComputerSystem class, parent class for Linux Windows subclasses
    """
    def __init__(self, ip, year, os):
        """ComputerSystem constructor

        Args:
            ip (str): ip address assigned to computer system
            year (int): year the computer was purchased
            os (str): operating system installed on computer
        """
        self.ip = ip
        self.os = os
        self._yearPurchased = year  

    @property
    def yearPurchased(self):
        """
        Returns the year the computer was purchased

        Returns:
            int: year the computer was purchased
        """
        return self._yearPurchased
    

    def getSpace(self):
        """
        Required implemention by subclasses

        Raises:
            NotImplementedError: if the subclass does not override this method
        """
        raise NotImplementedError("getSpace() must be overridden")

    def getStorageText(self):
        """
        Returns the amount of storage space available on system

        Returns:
            str: storage space 
        """
        return str(self.getSpace()) + "GB"
    
    def getIP(self):
        return self.ip


class Linux(ComputerSystem):
    """
    Linux class, subclass of computersystem
    """
    def __init__(self, ip, year, os, fsGB):
        """Linux constructor

        Args:
            ip (string): ip address of computer
            year (int): year that computer was purchased
            os (string): operating system installed on computer
            fsGB (string): file system space property
        """
        super().__init__(ip, year, os)
        self.fsGB = fsGB

    def getSpace(self):
        """
        Return file system space property in the integer form 

        Returns:
            int: file system space property
        """
        return self.fsGB

    def getStorageText(self):
        """Return file system space in the string form 

        Returns:
            str: file system space 
        """
        return "Filesystem: " + str(self.fsGB) + "GB"


class Windows(ComputerSystem):
    """Windows class, subclass of computer system"""
    def __init__(self, ip, year, os, cGB):
        """Windows constructor

        Args:
            ip (string): ip address of the computer 
            year (int): year the computer was purchased
            os (string): the operating system installed on the computer
            cGB (int): C drive space property
        """
        super().__init__(ip, year, os)
        self.cGB = cGB

    def getSpace(self):
        """Returns c drive space property in integer form 

        Returns:
            int: c drive space property
        """
        return self.cGB

    def getStorageText(self):
        """Returns c drive space property in text form 

        Returns:
            string: c drive space property
        """
        return "C drive: " + str(self.cGB) + " GB"




