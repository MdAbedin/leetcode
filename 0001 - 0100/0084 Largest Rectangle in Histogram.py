def Build_SparseTable (array : List[int], sparse_table : List[List[int]]) :
    rows = len(array)
    cols = len(sparse_table[0])

    for r in range(rows) :
        sparse_table[r][0] = array[r]

    for c in range(1, cols+1) :
        _range = (1<<c)
        r = 0
        while (r + _range <= rows) :
            sparse_table[r][c] = min (sparse_table[r][c-1],
                                      sparse_table[r+(1<<(c-1))][c-1])
            r += 1

def RMQ (left : int, right : int, sparse_table : List[List[int]]) :
    power_of_2 = int (math.log2(right + 1 - left))
    x = right + 1 - (1 << power_of_2)

    if (sparse_table[left][power_of_2] <= sparse_table[right + 1 - ( 1 << power_of_2 )][power_of_2]): return sparse_table[left][power_of_2]
    else: return sparse_table[right + 1 - ( 1 << power_of_2)][power_of_2]

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [[h,i] for i,h in enumerate(heights)]
        sparse_table = [[0]*(ceil(log2(len(heights)))+1) for i in range(len(heights))]
        Build_SparseTable(heights,sparse_table)

        def solve(l,r):
            if r < l:
                return 0
            else:
                m,mi = RMQ(l,r,sparse_table)
                return max(m*(r-l+1),solve(l,mi-1),solve(mi+1,r))

        return solve(0,len(heights)-1)
