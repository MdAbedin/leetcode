class Solution:
    def firstBadVersion(self, n: int) -> int:
        return bisect_left(range(1,n+1),True,key=isBadVersion)+1
