class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9+7
        seat_indexes = [i for i,c in enumerate(corridor) if c == "S"]
        
        return 0 if not seat_indexes or len(seat_indexes)%2 == 1 else prod(seat_indexes[i]-seat_indexes[i-1] for i in range(2,len(seat_indexes),2))%MOD
