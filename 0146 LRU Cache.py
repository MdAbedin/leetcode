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
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ll = DoublyLinkedList()
        self.maps = dict()

    def get(self, key: int) -> int:
        return self.put(key, self.maps[key].data[1]) if key in self.maps else -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            self.maps[key] = self.ll.append([self.ll.remove(self.maps[key]).data[0], value])
            return value
        else:
            if len(self.ll) == self.capacity:
                del self.maps[self.ll.popleft().data[0]]
            
            self.maps[key] = self.ll.append([key,value])
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
