class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return max((str1[:size] for size in range(1,min(len(str1),len(str2))+1) if all({s[i:i+size] for i in range(0,len(s),size)} == {str1[:size]} for s in (str1,str2))), default = "")
