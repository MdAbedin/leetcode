class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        D = defaultdict(int)
        
        for v,w in items1:
            D[v] += w
            
        for v,w in items2:
            D[v] += w
            
        return sorted(list(D.items()))
