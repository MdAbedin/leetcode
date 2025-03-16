class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        return bisect_left(range(10**14+1),True,key = lambda t: sum(floor(sqrt(t/r)) for r in ranks) >= cars)
