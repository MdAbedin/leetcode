class Solution:
    def largestOddNumber(self, num: str) -> str:
        digits = set(num)
        
        if not any(x in digits for x in ["1","3","5","7","9"]):
            return ""
        
        for i in reversed(range(len(num))):
            if num[i] in ["1","3","5","7","9"]:
                return num[:i+1]
