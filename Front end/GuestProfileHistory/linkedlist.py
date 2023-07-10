class Node:
    def __init__(self, data=None):
        self._item = data
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None
    
    def append(self, data):
        new_node = Node(data)
        if(self._head is None):
            self._head = new_node
        else:
            ele = self._head
            while ele._next is not None:
                ele = ele._next
            ele._next = new_node

    def __getitem__(self, index):
        element = self._head
        for i in range(index):
            element = element._next
        return element._item
    
    def display(self):
        ele = self._head
        while ele is not None:
            print(ele._item, "-->", end="")
            ele = ele._next
    
    def __str__(self):
        string = "[ "
        ele = self._head
        while ele is not None:
            string += str(ele._item) + " "
            ele = ele._next
        string += "]"
        return string
    
    def search_phno(self, phno):
        ele = self._head
        while ele is not None:
            if(ele._item[1] == str(phno)):
                return ele._item
            ele = ele._next
        return 

            