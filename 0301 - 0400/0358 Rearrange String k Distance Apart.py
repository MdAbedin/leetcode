class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counts = Counter(s).most_common()
        max_count = counts[0][1]
        groups = [[] for i in range(max_count)]
        cur = 0
        
        for char, count in counts:
            if count >= max_count-1:
                for i in range(count):
                    groups[i].append(char)
            else:
                for i in range(count):
                    groups[cur].append(char)
                    cur += 1
                    cur %= len(groups)-1
                    
        if len(groups)>=2 and len(groups[-2]) < k: return ""
        
        return "".join(["".join(g) for g in groups])
