from typing import Iterator


class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class LineList:
    # Constructor
    def __init__(self):
        self.head = None
    
    # Inserts in the end
    def insert(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return

        currNode = self.head
        while(currNode.next):
            currNode = currNode.next
        currNode.next=NewNode
    
    # Returns a specific item
    def __getitem__(self, key):
        currKey = 0
        currNode = self.head
        while(currNode.next and currKey != key):
            currNode = currNode.next
            currKey += 1
        return currNode.data

    # Returns an entire list
    def __str__(self):
        out = "\tList of Lines:"
        currNode = self.head
        counter = 1
        while currNode is not None:
            out += "\n %d: " % counter
            out += str(currNode.data)
            currNode = currNode.next
            counter += 1
        return out

    # Found this implementation online. Need to ask Abba bout it
    # def __iter__(self):
    #     current = self.head
    #     while current is not None:
    #         yield current.data
    #         current = current.next

    # def __str__(self):
    #     return str(list(self))