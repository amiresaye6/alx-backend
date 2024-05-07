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
            # try:
            #     # item is used before
            #     self.__frequancy[key] += 1
            # except Exception:
            #     # item is first time used
            #     self.__frequancy[key] = 1
            if key in self.__frequancy.keys():
                self.__frequancy[key] += 1
            else:
                self.__frequancy[key] = 1
            if key in self.__cache_array:
                for i in range(len(self.__cache_array)):
                    if key == self.__cache_array[i]:
                        self.__cache_array.pop(i)
                        self.__cache_array.append(key)
            else:
                self.__cache_array.append(key)
            if len(self.__cache_array) > self.MAX_ITEMS:
                # discard the least frequently used first
                l = min(self.__frequancy.values())
                unique_values_count = len(set(self.__frequancy.values()))
                if unique_values_count < len(self.__frequancy):
                    # means there is more than lfu key
                    same_count = []
                    for k, v in self.__frequancy.items():
                        if l == v:
                            # the key with the lfu value
                            same_count.append(k)
                    i = 0
                    for rk in same_count:
                        if self.__cache_array[i] == rk:
                            print("DISCARD: {}".format(self.__cache_array[i]))
                            del(self.cache_data[self.__cache_array.pop(i)])
                            del(self.__frequancy[rk])
                            break
                        i += 1
                else:
                    print("DISCARD: {}".format(self.__cache_array[0]))
                    del(self.cache_data[self.__cache_array.pop(0)])
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


my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()

my_cache.pr()
