"""
Project 4: Hash Table from Scratch
Part of the freeCodeCamp "Python Certification" (Python v9)

Key Features:
- Custom Hashing Algorithm: Implements a Unicode-summation based hashing function.
- Collision Resolution: Uses a nested dictionary structure to handle potential hash collisions.
- Core Data Structure Operations: Manual implementation of Add, Remove, and Lookup (Search).
- Data Integrity: Safe handling of non-existent keys during removal or lookup.
"""

class HashTable:
    def __init__(self):
        self.collection = {} # self.collection is the bucket array of the hash table

    def hash(self, key_string):  # calculate the hash value of the key
        hashed_value = 0
        for i in key_string:
            hashed_value += ord(i)  # the hashing function will be simple: it will sum the Unicode values of each character in the key.
        return hashed_value

    def add(self,key,value):
        original_dictionary = dict([(key, value)])
        new_key = self.hash(key)
        if new_key not in self.collection:
            self.collection.update(dict([(new_key,original_dictionary)])) # In the bucket array (a dict), key is hash value, value is an inner dict
        else: # if hash value already exists in bucket array, update the value of key-value pair of bucket array to include the new key-pair of the
            # inner dict
            self.collection[new_key].update({key:value})

    def remove(self,key):
        new_key = self.hash(key)
        if new_key not in self.collection:  # If key(hash value) of bucket array doesn't exist, key of the inner dict doesn't exist as well
            return
        else:
            if key in self.collection[new_key]: # Confirm if the key exists in the collection. (her key is the key of inner dict)
                del self.collection[new_key][key] # remove the key-value pair of inner dict, don't need to retrieve the deleted value
            else:  # If the key (of inner dict) does not exist in the collection, it should not raise an error or remove anything.
                return

    def lookup(self,key):
        new_key = self.hash(key)
        if new_key not in self.collection: # If the key (of inner dict) does not exist in the collection, it should return None.
            return None
        else:
            if key in self.collection[new_key]:
                return self.collection[new_key][key]  # return the corresponding value stored inside the hash table (here the value is the value of
                # key-value pair of the inner dict.
            else:
                return None # If the key (of inner dict) does not exist in the collection, it should return None.
