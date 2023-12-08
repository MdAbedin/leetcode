class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return [s2 for s2,c in Counter(s[i-9:i+1] for i in range(9,len(s))).items() if c >= 2]
