class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(a-b) for a,b in zip(*map(sorted,[seats,students])))
