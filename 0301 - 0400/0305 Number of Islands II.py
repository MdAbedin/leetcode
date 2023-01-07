class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(x):
            if x != parents[x]: parents[x] = find(parents[x])
            return parents[x]

        def union(a,b): parents[find(a)] = find(b)

        parents = {}
        islands = 0
        answers = []

        for r,c in positions:
            if (r,c) not in parents:
                parents[(r,c)] = (r,c)
                islands += 1

                for r2,c2 in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                    if (r2,c2) in parents and find((r,c)) != find((r2,c2)):
                        islands -= 1
                        union((r,c),(r2,c2))
                
            answers.append(islands)
        
        return answers
