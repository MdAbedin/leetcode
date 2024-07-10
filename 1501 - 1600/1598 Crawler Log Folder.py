class Solution:
    def minOperations(self, logs: List[str]) -> int:
        return reduce(lambda l,x: max(0,l+[1,-1,0][(x == "../")-(x == "./")]),logs,0)
