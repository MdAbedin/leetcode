class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = "".join(map(str.upper,"".join(s.split("-"))[::-1]))
        groups = [chars[i:i+k] for i in range(0,len(chars),k)]
        return "-".join(g[::-1] for g in groups[::-1])
