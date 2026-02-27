"""
File: linked.py
"""

class Node:
    def __init__(self, data):
        """
        Constructor for Node class
        """
        self.data = data
        self.next = None


class LinkedComputer:
    def __init__(self):
        """
        Constructor for LinkedComputer class
        """
        self.head = None
    
    def add(self, compObject):
        """
        Method that adds a ComputerSystem object to linked list based on year of purchase, oldest to newest 

        """
        new_node = Node(compObject)
        #if linked list is empty or the new computer is older than the head, insert at the beginning
        if self.head is None or compObject.getYearPurchased() < self.head.data.getYearPurchased():
            new_node.next = self.head #point the new node's next to the current head
            self.head = new_node #update head to the new node
        else:
            current = self.head
            #keep traverse as long as next node exists and new comp is newer than the next node's comp
            while current.next is not None and compObject.getYearPurchased() >= current.next.data.getYearPurchased():
                current = current.next
            
            #we have reached end of the list or found a node with a newer comp
            new_node.next = current.next #point new node's next to the current node's next
            current.next = new_node #point the current node's next to the new node


    def remove(self):
        """
        Method that removes and returns the front object (oldest computer) from linked list
        """
        if self.head is None:
            return None #list is empty so return None
        
        removed_computer = self.head.data #store data of the head node to return later
        self.head = self.head.next #update head to the next node; delete old head node
        return removed_computer #return the removed comp object

