class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        R,C = len(matrix),len(matrix[0])
        ans = 0

        for size in range(1,R+1):
            for r in range(size-1,R):
                psum_counts = Counter({0:1})
                psum = 0

                for c in range(C):
                    psum += sum(matrix[r2][c] for r2 in range(r-size+1,r+1))
                    ans += psum_counts[psum-target]
                    psum_counts[psum] += 1

        return ans
