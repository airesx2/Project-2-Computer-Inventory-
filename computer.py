"""
File: computer.py
Authors: Taran M, Arieana L 
Assignment: Project 2: Computer Inventory Using Linked Structure and Inheritance

"""


class ComputerSystem:
    def __init__(self, ip, year, os):
        self.ip = ip
        self.os = os
        self.__yearPurchased = year  

    def getYearPurchased(self):
        return self.__yearPurchased

    def getSpace(self):
        raise NotImplementedError("getSpace() must be overridden")

    def getStorageText(self):
        return str(self.getSpace()) + "GB"


class Linux(ComputerSystem):
    def __init__(self, ip, year, os, fsGB):
        super().__init__(ip, year, os)
        self.fsGB = fsGB

    def getSpace(self):
        return self.fsGB

    def getStorageText(self):
        return "Filesystem: " + str(self.fsGB) + "GB"


class Windows(ComputerSystem):
    def __init__(self, ip, year, os, cGB):
        super().__init__(ip, year, os)
        self.cGB = cGB

    def getSpace(self):
        return self.cGB

    def getStorageText(self):
        return "C drive: " + str(self.cGB) + " GB"




