class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for size in range(len(strs[0]),-1,-1):
            if all(string.startswith(strs[0][:size]) for string in strs): return strs[0][:size]
