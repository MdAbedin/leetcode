class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        seq = list(s[:10])
        counts = defaultdict(int)
        counts[''.join(seq)] = 1
        
        for i in range(10,len(s)):
            for j in range(9):
                seq[j] = seq[j+1]
                
            seq[-1] = s[i]
            counts[''.join(seq)] += 1
            
        return [seq for seq in counts if counts[seq] >= 2]
