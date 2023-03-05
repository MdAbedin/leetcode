class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0

        indexes = defaultdict(set)
        for i,num in enumerate(arr):
            indexes[num].add(i)

        bfs = deque([[0,0]])
        seen = {0}
        seen2 = set()

        while bfs:
            i,moves = bfs.popleft()

            for j in [i-1,i+1]:
                if j in range(len(arr)) and j not in seen:
                    if j == len(arr)-1: return moves+1
                    seen.add(j)
                    bfs.append([j,moves+1])

            if arr[i] not in seen2:
                seen2.add(arr[i])
                
                for j in indexes[arr[i]]:
                    if j in range(len(arr)) and j not in seen:
                        if j == len(arr)-1: return moves+1
                        seen.add(j)
                        bfs.append([j,moves+1])
