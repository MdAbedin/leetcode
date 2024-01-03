class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        return all({"0":"0","1":"1","6":"9","8":"8","9":"6"}.get(d1) == d2 for d1,d2 in zip(str(num),str(num)[::-1]))
