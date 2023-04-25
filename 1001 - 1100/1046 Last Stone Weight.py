class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = list(map(neg,stones))
        heapify(pq)

        while len(pq) > 1:
            y,x = -heappop(pq),-heappop(pq)
            if y != x: heappush(pq, -(y-x))

        return 0 if not pq else -pq[0]
