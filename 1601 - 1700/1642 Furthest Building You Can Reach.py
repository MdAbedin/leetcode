class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []

        for i,(h1,h2) in enumerate(pairwise(heights)):
            if h2 > h1: heappush(pq,h2-h1)
            if len(pq) > ladders: bricks -= heappop(pq)
            if bricks < 0: return i

        return len(heights)-1
