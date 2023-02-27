class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(r1,c1,r2,c2):
            if len({grid[r][c] for r in range(r1,r2+1) for c in range(c1,c2+1)}) == 1:
                return Node(grid[r1][c1], True, None, None, None, None)

            return Node(0,False,helper(r1,c1,(r1+r2)//2,(c1+c2)//2),helper(r1,(c1+c2)//2+1,(r1+r2)//2,c2),helper((r1+r2)//2+1,c1,r2,(c1+c2)//2),helper((r1+r2)//2+1,(c1+c2)//2+1,r2,c2))

        return helper(0,0,len(grid)-1,len(grid)-1)
