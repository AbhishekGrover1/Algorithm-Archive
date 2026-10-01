import random

class RandomizedCollection(object):

    def __init__(self):
        # Stores the actual values to allow O(1) random retrieval
        self.vals = []
        # Maps a value to a set of its indices in self.vals
        self.idxs = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.idxs:
            self.idxs[val] = set()
            
        # Add the new index to the set
        self.idxs[val].add(len(self.vals))
        self.vals.append(val)
        
        # Return True if this is the first time the item is inserted
        return len(self.idxs[val]) == 1

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # If the value doesn't exist or its set is empty
        if val not in self.idxs or not self.idxs[val]:
            return False
        
        # Get one of the indices of the value we want to remove
        idx_to_remove = self.idxs[val].pop()
        
        # Get the value and index of the last element in the list
        last_val = self.vals[-1]
        last_idx = len(self.vals) - 1
        
        # Swap the element to remove with the last element
        self.vals[idx_to_remove] = last_val
        
        # Update the hash map for the swapped last element
        self.idxs[last_val].add(idx_to_remove)
        self.idxs[last_val].discard(last_idx)
        
        # Remove the last element from the list
        self.vals.pop()
        
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.vals)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()