class DoublyLinkedList:
    class Node:
        def __init__(self, data = None):
            self.data = data
            self.prev = None
            self.next = None
            
    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
        
    def __len__(self):
        return self.length
    
    def remove(self, node):
        self.length -= 1
        node.prev.next, node.next.prev = node.next, node.prev
        
        return node

    def append(self, data):
        new_node = self.Node(data)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        new_node.prev.next = new_node
        new_node.next.prev = new_node
        self.length += 1
        
        return new_node
    
    def popleft(self):
        return self.remove(self.head.next)
    
    def peekleft(self):
        return self.head.next

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dll = DoublyLinkedList()
        self.maps = dict()
        
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.dll.peekleft().data if len(self.dll) else -1

    def add(self, value: int) -> None:
        if value in self.maps:
            if self.maps[value] is not None:
                self.dll.remove(self.maps[value])
                self.maps[value] = None
        else:
            self.maps[value] = self.dll.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
