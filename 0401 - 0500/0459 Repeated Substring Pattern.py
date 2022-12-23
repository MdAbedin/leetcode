class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for length in range(1,len(s)):
            if len(s) % length == 0:
                if all(s[length*m : length*(m+1)] == s[:length] for m in range(len(s)//length)):
                    return True

        return False
