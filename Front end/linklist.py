class Node:
    def __init__(self, data=None):
        self._item = data
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = Node()
    
    def append(self, data):
        new_node = Node(data)
        new_node._next = self._head._next
        self._head._next = new_node
    
    def display(self):
        ele = self._head
        while ele._next is not None:
            ele = ele._next
            print(ele._item, "-->", end="")
    


    