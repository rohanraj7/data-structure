class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash_function(key)

        while self.keys[index] is not None and self.keys[index] != key:
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self._hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.size

        return None

    def remove(self, key):
        index = self._hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return

            index = (index + 1) % self.size
# Create a hash table of size 10
ht = HashTable(10)

# Add some key-value pairs
ht.put('apple', 3)
ht.put('banana', 2)
ht.put('orange', 5)

# Get the value associated with a key
print(ht.get('banana'))  # Output: 2

# Remove a key-value pair
ht.remove('orange')

# Try to get the value associated with the removed key
print(ht.get('orange'))  # Output: None
