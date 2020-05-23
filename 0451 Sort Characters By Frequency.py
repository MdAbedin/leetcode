class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        chars = defaultdict(list)
        
        for char in counts:
            chars[counts[char]].append(char)
            
        ans = ''
        
        for count in sorted(chars.keys(),reverse=True):
            for char in chars[count]:
                ans += char*count
                
        return ans
