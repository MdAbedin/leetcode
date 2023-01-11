class Solution:
   def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counts = Counter(nums)
        nums = deque(sorted(counts))

        while nums:
            if len(nums) < k: return False

            for i in range(k):
                if counts[nums[0]+i] == 0: return False
                counts[nums[0]+i] -= 1

            while nums and counts[nums[0]] == 0: nums.popleft()

        return True 
