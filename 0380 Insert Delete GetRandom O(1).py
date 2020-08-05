class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.nums_dict = dict()
        self.deleted = 0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.nums_dict:
          self.nums.append(val)
          self.nums_dict[val] = len(self.nums)-1
          
          return True
          
        if val in self.nums_dict and self.nums_dict[val] < self.deleted:
          last_deleted = self.nums[self.deleted-1]
          val_i = self.nums_dict[val]
          
          self.nums[self.deleted-1], self.nums[self.nums_dict[val]] = val, last_deleted
          self.nums_dict[last_deleted], self.nums_dict[val] = val_i, self.deleted-1
          self.deleted -= 1
          
          return True
        
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.nums_dict and self.nums_dict[val] >= self.deleted:
          first_stored = self.nums[self.deleted]
          val_i = self.nums_dict[val]
          
          self.nums[self.deleted], self.nums[val_i] = val, first_stored
          self.nums_dict[first_stored], self.nums_dict[val] = val_i, self.deleted
          self.deleted += 1
          
          return True
        
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[randint(self.deleted, len(self.nums)-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
