'''/*
 * LRU Cache
 * LRU = > least recently used
 * cache. generally, the more items something can store, the slower it is to retrieve items from it
 * caches for memory: L1 and L2 cache(these are managed by your operating systeM)
 * memory is much faster than disk
 * LRU = > cache policy. this policy determines how we insert things into the cache and when we kick old stuff out
 * always insert new things in , and bump out the least recently used item in the cache
 * K = > V pairs
 */
 '''
'''
use a dictionary where the key will be the key, value will the order in which
could have a tuple (key, value) as my_dict[key] and value will be the order in which it is in
I always need to keep track of least recently used aka oldest, I would need to update the ordering of the rest of the items in cache.
use doubly linked list to keep track of the order of the keys


At capacity
how can we get to keys in the middle of the doubly linked list quickly
'''

[0,1,2,3,4]
from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity, source):
        self.capacity = capacity
        self.source = source
        self.dict = OrderedDict()

    def get(key):
        # IF ITS IN THE CACHE< JUST GIVE IT BACK TO THE USER, reorder cache
        # IF NOT, get it from source. source.get(key)
        # add to cache at top if not at capacity,
        # otherwise, bump out least recently used
        if key in self.dict:
          val = self.dict[key]
          del self.dict[key]
          self.dict[key] = val
          return val
        
        val = source.get(key)

        self.dict[key] = val
        if len(self.dict > capacity):
          OrderedDict.popitem(last=True)
          
        return val
          

        



        

