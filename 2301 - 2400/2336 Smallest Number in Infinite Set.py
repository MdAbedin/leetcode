class SmallestInfiniteSet:
    def __init__(self):
        self.not_contained = set()
        self.pq = []
        self.min_unused = 1        

    def popSmallest(self) -> int:
        if not self.pq:
            ans = self.min_unused
            self.min_unused += 1
        else:
            ans = heappop(self.pq)

        self.not_contained.add(ans)

        return ans

    def addBack(self, num: int) -> None:
        if num not in self.not_contained: return
        self.not_contained.remove(num)
        heappush(self.pq, num)
