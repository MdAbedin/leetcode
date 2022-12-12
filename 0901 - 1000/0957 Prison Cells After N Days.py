class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:      
      seen = set()
      layouts = []
      
      for i in range(N):
        copy = cells[::]

        for j in range(1,len(copy)-1):
          cells[j] = 1 if copy[j-1]+copy[j+1] != 1 else 0
        
        if i == 0: cells[0] = cells[-1] = 0
        
        layout = ''.join(map(str, cells))
        
        if layout in seen:
          break
          
        seen.add(layout)
        layouts.append(layout)
        
      return layouts[(N-1)%len(seen)]
