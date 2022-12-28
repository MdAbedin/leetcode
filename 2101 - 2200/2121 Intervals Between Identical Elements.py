class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        info = dict()
        ans = [0]*len(arr)

        for i,num in enumerate(arr):
            if num not in info:
                info[num] = [i,1,0]
            else:
                j,count,add = info[num]
                info[num] = [i,count+1,add + count*(i-j)]
                ans[i] += info[num][2]

        info = dict()

        for i,num in enumerate(arr[::-1]):
            if num not in info:
                info[num] = [i,1,0]
            else:
                j,count,add = info[num]
                info[num] = [i,count+1,add + count*(i-j)]
                ans[~i] += info[num][2]

        return ans
