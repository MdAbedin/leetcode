class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def union(a,b):
            parents[find(a)] = find(b)
            
        def find(x):
            if parents[x] != x: parents[x] = find(parents[x])
            return parents[x]
        
        parents = dict(zip(ascii_lowercase,ascii_lowercase))
        
        for c1,c2 in zip(s1,s2):
            union(c1,c2)
            
        followers = defaultdict(list)
        
        for letter in ascii_lowercase:
            followers[find(letter)].append(letter)
                
        return "".join(min(followers[find(c)]) for c in baseStr)
