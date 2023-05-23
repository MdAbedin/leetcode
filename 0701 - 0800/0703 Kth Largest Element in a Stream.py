class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k

        self.pq = nums

        heapify(self.pq)

        while len(self.pq) > k: heappop(self.pq)

    def add(self, val: int) -> int:

        heappush(self.pq,val)

        if len(self.pq) > self.k: heappop(self.pq)

        return self.pq[0]
