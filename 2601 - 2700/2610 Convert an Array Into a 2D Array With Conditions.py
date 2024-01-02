class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        ans = []

        while True:
            ans.append([num for num,count in counts.items() if count != 0])
            for num in list(counts): counts[num] = max(0,counts[num]-1)
            if set(counts.values()) == {0}: return ans
