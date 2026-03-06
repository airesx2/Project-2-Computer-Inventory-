"""
File: linked.py
Description:
Linked structure called LinkedComputer that keeps track of ComputerSystem objects with add and remove methods
"""

class Node:
    """
    Node class for linked list implementation
    """
    def __init__(self, data):
        """
        Constructor for Node class
        Args:
            data (ComputerSystem): the computer object stored in this node
        """
        self.data = data
        self.next = None
    


class LinkedComputer:
    """
    LinkedComputer class that implements a linked list to store ComputerSystem objects
    """
    def __init__(self):
        """
        Constructor for LinkedComputer class
        """
        self.head = None
        self.count = 0
    
    def add(self, compObject):
        """
        Method that adds a ComputerSystem object to linked list based on year of purchase, oldest to newest 
        Args:
            compObject (ComputerSystem): the computer object to be added to the linked list

        """
        self.count += 1
        new_node = Node(compObject)
        #if linked list is empty or the new computer is older than the head, insert at the beginning
        if self.head is None or compObject.yearPurchased < self.head.data.yearPurchased:
            new_node.next = self.head #point the new node's next to the current head
            self.head = new_node #update head to the new node
        else:
            current = self.head
            #keep traverse as long as next node exists and new comp is newer than the next node's comp
            while current.next is not None and compObject.yearPurchased >= current.next.data.yearPurchased:
                current = current.next
            
            #we have reached end of the list or found a node with a newer comp
            new_node.next = current.next #point new node's next to the current node's next
            current.next = new_node #point the current node's next to the new node


    def remove(self):
        """Method that removes the oldest computer from the linked list and returns it

        Returns:
            ComputerSystem: the removed computer object (or None list is empty)
        """
        #if the linked list is empty, return None
        if self.head is None:
            return None 
        
        removed_computer = self.head.data #store data of the head node to return later
        self.head = self.head.next #update head to the next node; delete old head node
        self.count -= 1 #decrement count of nodes in the list
        return removed_computer #return the removed comp object
    
    def len(self):
        """Returns the number of nodes in the linked list

        Returns:
            int: number of nodes in the linked list
        """
        return self.count
    
    

