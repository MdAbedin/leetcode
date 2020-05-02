class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = defaultdict(set)
        
        for i in range(len(ppid)):
            children[ppid[i]].add(pid[i])
            
        bfs = deque([kill])
        ans = []
        
        while bfs:
            cur = bfs.popleft()
            ans.append(cur)
            
            for child in children[cur]:
                bfs.append(child)
            
        return ans
