class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = {start}
        bfs = deque([[start, 0]])
        bank = set(bank)
        
        while bfs:
            genes, num_mutations = bfs.popleft()
            
            for i in range(8):
                for char in ['A','C','G','T']:
                    mutation = genes[:i]+char+genes[i+1:]
                    
                    if mutation in bank and mutation == end:
                        return num_mutations+1
                    
                    if mutation in bank and mutation not in visited:
                        bfs.append([mutation, num_mutations+1])
                        visited.add(mutation)
        
        return -1
