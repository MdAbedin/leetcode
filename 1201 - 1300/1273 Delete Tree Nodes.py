class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        children = defaultdict(list)
        root = None
        
        for child,parent1 in enumerate(parent):
            if parent1 != -1:
                children[parent1].append(child)
            else:
                root = child
                
        bfs = deque([root])
        reverse_bfs = deque()
        
        while bfs:
            cur = bfs.popleft()
            reverse_bfs.append(cur)
            for child in children[cur]:
                bfs.append(child)

        sums = defaultdict(int)
        sizes = defaultdict(int)
        
        while reverse_bfs:
            cur = reverse_bfs.pop()
            sums[cur] = value[cur]
            sizes[cur] = 1
            
            for child in children[cur]:
                sums[cur] += sums[child]
                sizes[cur] += sizes[child]

            if sums[cur] == 0: sizes[cur] = 0
                
        return sizes[root]
