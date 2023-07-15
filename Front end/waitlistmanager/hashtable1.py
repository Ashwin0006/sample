class HashTable:
    def __init__(self, capacity = 10):
        self._items = [None] * capacity
        self._cap = capacity
    
    def hash_func(self, key, probe):
        if(key.isdigit()):
            return (key + probe) % self._cap
        else:
            if(len(key) >= 3):
                val = 1 * ord(key[0]) + 27 * ord(key[1]) + 729 * ord(key[2])
                return (val + probe) % self._cap
            else:
                val = 0
                for i in range(len(key)):
                    val += (27**i) * ord(key[i])
                return (val + probe) % self._cap           
    
    def resize(self):
        self._cap = self._cap * 2
        temp = [None] * self._cap
        for i in range(len(self._items)):
            if self._items[i] is not None:
                temp[i] = self._items[i]
        self._items = temp

    def add(self, key, val):
        if(None not in self._items):
            self.resize()
        probe = 0
        while(1):
            index = self.hash_func(key, probe)
            if self._items[index] is None:
                self._items[index] = val
                break
            probe = pow(probe+1, 2)
    
    def __getitem__(self, key):
        probe = 0
        count = 0
        while(1):
            index = self.hash_func(key, probe)
            if(self._items[index] != None):
                return self._items[index]
            probe = pow(probe+1, 2)
            count += 1
            if(count >= self._cap):
                print("Element is Not present")
                return False
            
    def __str__(self):
        return str(self._items)
    
        

