class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values, self.use_counts = {}, {}
        self.prevs, self.nexts = {}, {}
        self.LFU = None

    def update_use_count(self, key):
        value = self.values[key]
        use_count = self.use_counts[key]
        self.delete(key)
        self.add(key, value, use_count+1)
        
        head,tail = (use_count,"head"),(use_count,"tail")
        if self.LFU == key:
            if self.nexts[head] != tail: self.LFU = self.nexts[head]
            else: self.LFU = self.nexts[(use_count+1,"head")]
    
    def delete(self, key):
        self.values.pop(key)
        self.use_counts.pop(key)
        self.nexts[self.prevs[key]] = self.nexts[key]
        self.prevs[self.nexts[key]] = self.prevs[key]
    
    def add(self, key, value, use_count):
        self.values[key] = value
        self.use_counts[key] = use_count
        
        head,tail = (use_count,"head"),(use_count,"tail")
        if head not in self.nexts:
            self.nexts[head] = tail
            self.prevs[tail] = head
            
        last = self.prevs[tail]
        self.prevs[key], self.nexts[key] = last, tail
        self.nexts[last] = self.prevs[tail] = key
    
    def get(self, key: int) -> int:
        if key not in self.values: return -1
        self.update_use_count(key)
        return self.values[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        
        if key not in self.values:
            if len(self.values) == self.capacity: self.delete(self.LFU)
            self.add(key, value, 1)
            self.LFU = self.nexts[(1,"head")]
        else:
            self.update_use_count(key)
            self.values[key] = value
