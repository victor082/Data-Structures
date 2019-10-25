from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct 
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        # DLL to store the order
        self.order = DoublyLinkedList()
        # Dict storekey value pairs
        self.storage = dict()
        # current size
        self.size = 0
        # limit
        self.limit = limit

    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """

    def get(self, key):
        # pull the value out of the dictionary using the key
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_front(node)
            return node.value[1]
        # Update the position of the list
        else:
            return None
        # or return none

    """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """

    def set(self, key, value):
        # Add pair to the cache - add to the dict and add it nodes/DLL
        if key in self.storage:  # update dict
            node = self.storage[key]
            # makes it easy to grab the key and value
            node.value = (key, value)
        # Marks as most recently used - Put in the head of the DLL
            self.order.move_to_front(node)
            return

        # If at max capacity, dump oldest - remove from tail of DLL
        if self.size == self.limit:
            # dump the oldest
            # Remove it from the linked list
            # remove it from the dictionary
            del self.storage(self.order.tail.value[0])
            self.order.remove_from_tail()
            self.size -= 1

        # Add pair to the cache - add to dict and it node/DLL
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.head
        self.size += 1
