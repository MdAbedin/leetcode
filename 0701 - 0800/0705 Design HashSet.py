class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [0]*int(1e6+1)

    def add(self, key: int) -> None:
        self.table[key] = 1

    def remove(self, key: int) -> None:
        self.table[key] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.table[key] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
