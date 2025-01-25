class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        l = sorted(enumerate(nums),key=itemgetter(1))
        i = 0

        for i2 in range(1,len(l)):
            if l[i2][1] - l[i2-1][1] > limit:
                for i3,num in zip(sorted(i for i,x in l[i:i2]),[x for i,x in l[i:i2]]): nums[i3] = num
                i = i2

        for i3,num in zip(sorted(i for i,_ in l[i:]),[x for _,x in l[i:]]): nums[i3] = num

        return nums
