class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = [1]
        for r1,r2 in zip(ratings,ratings[1:]): l.append(l[-1]+1 if r2 > r1 else 1)

        r = [1]
        for r1,r2 in zip(ratings[::-1],ratings[::-1][1:]): r.append(r[-1]+1 if r2 > r1 else 1)
        r.reverse()

        return sum(map(max,zip(l,r)))
