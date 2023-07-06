class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        nums = list(range(1,n+1))
        ans = []

        for i in range(n):
            ans.append(nums.pop(k//factorial(n-i-1)))
            k %= factorial(n-i-1)

        return "".join(map(str,ans))
