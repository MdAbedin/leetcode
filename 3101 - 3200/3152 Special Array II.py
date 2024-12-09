class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        streaks = [1]
        for num1,num2 in pairwise(nums): streaks.append(1 if num1%2 == num2%2 else streaks[-1]+1)
        return [streaks[r] >= r-l+1 for l,r in queries]
