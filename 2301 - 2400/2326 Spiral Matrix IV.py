class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        seen = set()
        r,c = 0,0
        dr,dc = 0,1
        ans = [[-1]*n for _ in range(m)]

        while head:
            ans[r][c] = head.val
            seen.add((r,c))
            if r+dr not in range(m) or c+dc not in range(n) or (r+dr,c+dc) in seen: dr,dc = dc,-dr
            r += dr
            c += dc
            head = head.next

        return ans
