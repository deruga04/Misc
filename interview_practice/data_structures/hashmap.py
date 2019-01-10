class HashTable:
    
    def __init__(self):
        self.M = 97
        self.keys = [None] * 97
        self.values = [None] * 97
        self.sentinel = Sentinel()

    def hash_func(self, x):
        hash_value = 0
        R = 31
        
        if isinstance(x, str):
            for i in range(len(x)):
                hash_value = (R * hash + x[i]) % self.M;

        if isinstance(x, int):
            hash_value = x % 97
        
        return hash_value

    def find_index_add(self, key):
        index = hashed_key = self.hash_func(key)
        steps = 0

        while not self.keys[index] == None or steps >= self.M:
            index += 1

        return index

    def find_index(self, key):
        index = hashed_key = self.hash_func(key)
        steps = 0

        while not self.keys[index] == None or steps >= self.M:
            if self.keys[index] == key:
                return index
            index += 1

        print('Key not found')

    def add(self, key, value):
        if not key in self.keys: 
            index = self.find_index_add(key)
            self.keys[index] = key
            self.values[index] = value
            print(f'added to index {index}')
        else:
            print('Key already exists')

    def remove(self, key):
        index = self.find_index(key)
        self.keys[index] = self.sentinel
        self.values[index] = self.sentinel
        
    def get(self, key):
        index = self.find_index(key)
        print(f'getting from index {index}')
        return self.values[index]

class Sentinel:
    def __init__(self):
        pass


h = HashTable()
h.add(1, 'banana')
h.add(1, 'apple')
print(h.get(1))
h.remove(1)
print(h.get(1))
