class HashTable:
    def __init__(self, capacity = 10):
        self._items = [None] * capacity
        self._cap = capacity
    
    def hash_func(self, key, probe):
        if(key.isdigit()):
            return (key + probe) % self._cap
        else:
            if(len(key) >= 3):
                val = int(str(key[0]) + str(key[2]))
                return val
            else:
                val = 0
                for i in range(len(key)):
                    val += (27**i) * ord(key[i])
                return (val + probe) % self._cap           

    
    def __getitem__(self, key):
        probe = 0
        index = self.hash_func(key, probe)
        return self._items[index]

    def __setitem__(self, key, val):
        probe = 0
        index = self.hash_func(key, probe)
        self._items[index] = val

            
    def __str__(self):
        return str(self._items)

