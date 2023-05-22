class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        nums2 = [[] for i in range(10**5+1)]

        

        for num,count in counts.items():

            nums2[count].append(num)

            

        ans = []

        

        for count in range(10**5,0,-1):

            for num in nums2[count]:

                ans.append(num)

                k -= 1

                if k == 0: return ans
