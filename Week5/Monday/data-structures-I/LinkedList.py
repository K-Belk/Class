####API####
# insert - add node to beginning (or end)
# search - find and return a given node
# remove - remove a given node
# size - return number of nodes
# is_empty - True if no nodes, False otherwise

import re


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.size_nodes = 0

    def insert(self, value):
        new_node = Node(value) 
        self.size_nodes += 1
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        return new_node

    def remove(self, element):
        if self.head.value == element:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.value != element:
                if current_node.next == None:
                    return "No such element in linked list"
                else:
                    previous_node = current_node
                    current_node = current_node.next
            previous_node.next = current_node.next
        self.size_nodes -= 1
        return f"{element} has been removed"

    def search(self, element):
        if self.head.value == element:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.value != element:
                if current_node.next == None:
                    return "No such element in linked list"
                else:
                    current_node = current_node.next
        return f"{element} has been found"


    def size(self):
        return self.size_nodes
        

    def is_empty(self):
        if self.size_nodes == 0:
            return True
        else:
            return False

