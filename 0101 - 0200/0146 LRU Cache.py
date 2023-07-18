class Node:
    def __init__(self, key = None, val = None, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head 
    
    def pop(self, node = None):
        if not node: node = self.tail.prev
        if node == self.head: return None

        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

        return node      

    def add_first(self, node):
        node.nxt = self.head.nxt
        node.prev = self.head
        
        node.prev.nxt = node
        node.nxt.prev = node
        
        return node
    
class LRUCache:
    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.DLL = DLL()
        self.capacity = capacity

    def get_node(self, key):
        return None if key not in self.key_to_node else self.DLL.add_first(self.DLL.pop(self.key_to_node[key]))
    
    def get(self, key: int) -> int:
        return node.val if (node := self.get_node(key)) else -1

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node: self.key_to_node[key] = self.DLL.add_first(Node(key,value))
        else: self.get_node(key).val = value
            
        if len(self.key_to_node) > self.capacity: self.key_to_node.pop(self.DLL.pop().key)
