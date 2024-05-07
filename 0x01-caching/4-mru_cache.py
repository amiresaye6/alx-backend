#!/usr/bin/env python3
"""
task: 4. MRU Caching

condition: mandatory

required:
Create a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent
init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    caching system class using most recently used algorithm
    """

    def __init__(self):
        """
        init constructor
        """
        super().__init__()
        self.__cache_array = []

    def put(self, key, item):
        """
        setter for the cache_data using mfu algorithm
        """
        if key is not None and item is not None:
            if key in self.__cache_array:
                # print("found")
                for i in range(len(self.__cache_array)):
                    if key == self.__cache_array[i]:
                        self.__cache_array.pop(i)
                        self.__cache_array.append(key)
            else:
                self.__cache_array.append(key)
            if len(self.__cache_array) > self.MAX_ITEMS:
                print("DISCARD: {}".format(
                    self.__cache_array[self.MAX_ITEMS - 1]))
                del(self.cache_data[self.__cache_array.pop(-2)])
            self.cache_data[key] = item

    def get(self, key):
        """
        getter for the cache_data[key]
        """
        try:
            if key in self.__cache_array:
                # print("found")
                for i in range(len(self.__cache_array)):
                    if key == self.__cache_array[i]:
                        self.__cache_array.pop(i)
                        self.__cache_array.append(key)
            return self.cache_data[key]
        except Exception:
            return None
