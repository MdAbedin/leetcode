class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        counts = Counter(ranks)
        return min(rank * (1+bisect_left(range(1,cars+1), True, key = lambda n: sum(floor(sqrt((rank*n**2)/rank2)) * counts[rank2] for rank2 in counts) >= cars))**2 for rank in counts)
