"""This module is a class called Queue() which is a datastructure.
   It also contains the functions to operate on the queue.
   This is a wrapper class using a list.

   Created on  Thursday 1st June

   Revised on Saturday 4th June 
   
   Original author : Ashwin Kumar.S <ashwinkumar2210738@ssn.edu.in>
"""



class Queue:
    """The queue is a datastructure that stores data at the end of datastructure and retrives
       data in the front end.It follows First-in-First-Out principle"""
    def __init__(self):
        self._items = []
        self._front = 0
    

    def enqueue(self, data):
        """Adds an element at the end of the queue."""
        self._items.append(data)
    
    def dequeue(self):
        """Removes an element at the front end of the queue."""
        if(len(self) != 0):
            ele = self._items[self._front]
            del self._items[self._front]
            self._front = 0
            return ele
        else:
            print("Queue is empty!")
            return 
        
    def __len__(self):
        return len(self._items)
    
    def getqueue(self):
        return self._items

