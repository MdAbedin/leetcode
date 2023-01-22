class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        for num in range(2**(len(s)-1)):
            indexes = [0] + [i+1 for i,c in enumerate(f"{num:b}".zfill(len(s)-1)) if c == "1"] + [len(s)]
            partition = [s[i1:i2] for i1,i2 in zip(indexes, indexes[1:])]
            if all(part == part[::-1] for part in partition): ans.append(partition)
        
        return ans
