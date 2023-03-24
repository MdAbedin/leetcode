class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parents = list(range(len(strs)))

        def find(x):
            if parents[x] != x: parents[x] = find(parents[x])
            return parents[x]

        def union(a,b):
            parents[find(a)] = find(b)

        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                diffs = [k for k in range(len(strs[i])) if strs[i][k] != strs[j][k]]
                
                if len(diffs) == 0:
                    union(i,j)
                elif len(diffs) == 2:
                    if strs[i][diffs[0]] == strs[j][diffs[1]] and strs[i][diffs[1]] == strs[j][diffs[0]]:
                        union(i,j)
                
        return len({find(i) for i in range(len(strs))})
