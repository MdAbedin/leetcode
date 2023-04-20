class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        indexes = defaultdict(list)
        for i,num in enumerate(nums): indexes[num].append(i)
            
        for num,indexes2 in indexes.items():
            dist = sum(indexes2[i] - indexes2[0] for i in range(1,len(indexes2)))
            ans[indexes2[0]] = dist
            
            for i1 in range(1,len(indexes2)):
                d = indexes2[i1]-indexes2[i1-1]
                dist -= (len(indexes2)-i1) * d
                dist += (i1) * d
                ans[indexes2[i1]] = dist
                
        return ans
