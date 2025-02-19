class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3*(2**(n-1)): return ""

        ans = ["bca"[(k > 2**n)-(k <= 2**(n-1))]]
        while k > 2**(n-1): k -= 2**(n-1)
        n -= 1

        while n:
            ans.append(("b" if ans[-1] == "a" else "a") if k <= 2**(n-1) else ("b" if ans[-1] == "c" else "c"))
            while k > 2**(n-1): k -= 2**(n-1)
            n -= 1

        return "".join(ans)
