"""
Implementation of Hash Table.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


class HashTable:
    """Hash table implementation and member functions.

    TIME COMPLEXITY (Search): Best:O(1), Average:O(1), Worst:O(n)
    TIME COMPLEXITY (Insert): Best:O(1), Average:O(1), Worst:O(n)
    TIME COMPLEXITY (Delete): Best:O(1), Average:O(1), Worst:O(n)
    SPACE COMPLEXITY: Worst: O(n)
    """

    def __init__(self, size):
        self.size = size
        self.slots = [None]*size
        self.data = [None]*size

    def put(self, key, value):

        hash_value = self.hash_function(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                rehash_value = self.rehash_function(hash_value, len(self.slots))
                while self.slots[rehash_value] is not None and self.slots[rehash_value] != key:
                    rehash_value = self.rehash_function(rehash_value, len(self.slots))
                if self.slots[rehash_value] is None:
                    self.slots[rehash_value] = key
                    self.data[rehash_value] = value
                else:
                    self.data[rehash_value] = value

    def get(self, key):

        hash_value = self.hash_function(key, len(self.slots))
        found = False
        stop = False
        position = hash_value
        data = None

        while self.slots[position] is not None and not found and not stop:
            position = self.rehash_function(position, len(self.slots))
            if self.slots[position] == key:
                data = self.data[position]
                found = True
            if position == hash_value:
                stop = True

        return data

    def hash_function(self, key, size):
        return key % size

    def rehash_function(self, old_hash, size):
        return (old_hash+1) % size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem(self, key):
        return self.get(key)
