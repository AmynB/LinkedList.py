# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:32:00 2016

@author: ab-src
@program: Linked List in Python
"""


#Linked List Class
class LinkedList(object):
    
    #Initialize head node
    def __init__(self, head=None):
        self.head = head
        
    #Insert new node, Insert new node in location if parameter given
    def insert(self, data, location=None):
        current_node = self.head
        if location == None:        
            new_node = Node(data)
            new_node.set_pointer(self.head)
            self.head = new_node
        elif isinstance(location, int):
            node_index = (self.size() - location) - 1 
            new_node = Node(data)
            count = 0
            while current_node and count <= node_index:
                if count == node_index:    
                    next_node = current_node.retrieve_next()
                    current_node.set_pointer(new_node)
                    new_node.set_pointer(next_node)
                    current_node = new_node    
                else:
                    current_node = current_node.retrieve_next()
                count += 1
            if count > node_index+1:
                print("Error: Index Out of List Range")
        else:
            print("Error: Location Must Be An Integer Number")
                
                    
    #Find size of Linked List
    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.retrieve_next()
        return count
    
    #Search for queried data
    def search(self, data):
        current_node = self.head
        found = False
        while current_node and found is False:
            if current_node.retrieve_node() == data:
                found = True
            else:
                current_node = current_node.retrieve_next()
        if current_node is None:
            print("Error: Cannot find Query")
        return current_node
    
    #List all elements in the linked list as an array
    def datalist(self):
        current_node = self.head
        listing = []
        while current_node and current_node.retrieve_node() is not None:
            listing.append(current_node.retrieve_node())
            current_node = current_node.retrieve_next()
        return list(reversed(listing))
    
    #Delete queried data
    def delete(self, data):
        current_node = self.head
        found = False
        previous_node = None
        while current_node and found is False:
            if current_node.retrieve_node() == data:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.retrieve_next()
        if current_node is None:
            print("Error: Cannot find Query")
        if previous_node is None:
            self.head = current_node.retrieve_next()
        else:
            previous_node.set_pointer(current_node.retrieve_next())
            
    #Delete all data in the list
    def clear(self):
        current_node = self.head
        while current_node:
            self.head = current_node.retrieve_next()
            previous_node = current_node
            current_node = previous_node.retrieve_next()
            previous_node = None
        self.head = None
        
#Node Object  Class   
class Node(object):
    
    #Initialize node
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    #Returns stored data in node
    def retrieve_node(self):
        return self.data
        
    #Returns the next node
    def retrieve_next(self):
        return self.next_node
    
    #Resets pointer to a new node
    def set_pointer(self, new_next):
        self.next_node = new_next
