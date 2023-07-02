from ctypes import py_object

class hashtable:
    def __init__(self, capacity = 10):
        self._items = (py_object * capacity)()
    
    def hash(self, val):
        pass
