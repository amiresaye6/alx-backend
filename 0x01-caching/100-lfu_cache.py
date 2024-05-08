#!/usr/bin/env python3
"""
task: 5. LFU Caching

condition: #advanced

required:
Create a class LFUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU algorithm to
discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    caching system class using least frequency used
    """

    def __init__(self):
        """
        init constructor
        """
        super().__init__()
        self.__cache_array = []
        self.__frequancy = {}

    def put(self, key, item):
        """
        setter for the cache_data using lfr algorithm
        """
        if key is not None and item is not None:
            if key in self.__cache_array:
                self.__frequancy[key] += 1
                for k in range(len(self.__cache_array)):
                    if key == self.__cache_array[k]:
                        self.__cache_array.pop(k)
                        self.__cache_array.append(key)
            else:
                if len(self.__cache_array) == self.MAX_ITEMS:
                    # reach the cache limit
                    # get the lru key and value
                    lru_value = min(self.__frequancy.values())
                    lru_array = []
                    for lru_k, lru_v in self.__frequancy.items():
                        if lru_v == lru_value:
                            lru_array.append(lru_k)  # add all keys with min v
                    # delete all key values from redcords
                    for del_key in self.__cache_array:
                        if del_key in lru_array:
                            print("DISCARD: {}".format(del_key))
                            # delete the stord key value from data
                            del(self.cache_data[del_key])
                            # delete the key val from freq dict
                            del(self.__frequancy[del_key])
                            # delete the key from cache array
                            for i in range(len(self.__cache_array)):
                                if self.__cache_array[i] == del_key:
                                    self.__cache_array.pop(i)
                                    break
                            break
                self.__frequancy[key] = 1
                self.__cache_array.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        getter for the cache_data[key]
        """
        try:
            if key in self.__cache_array:
                self.__frequancy[key] += 1
                for i in range(len(self.__cache_array)):
                    if key == self.__cache_array[i]:
                        self.__cache_array.pop(i)
                        self.__cache_array.append(key)
            return self.cache_data[key]
        except Exception:
            return None

    def pr(self):
        """
        helper function prints frequancy dictionary
        """
        print(self.__frequancy)
