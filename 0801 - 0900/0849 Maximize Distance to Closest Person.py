class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l_dists = [inf]
        for seat in seats:
            if seat == 1:
                l_dists.append(0)
            else:
                l_dists.append(l_dists[-1]+1)
        l_dists = l_dists[1:]

        r_dists = [inf]
        for seat in seats[::-1]:
            if seat == 1:
                r_dists.append(0)
            else:
                r_dists.append(r_dists[-1]+1)
        r_dists = r_dists[1:]
        r_dists.reverse()

        return max(min(ld,rd) for ld,rd,seat in zip(l_dists,r_dists,seats) if seat == 0)
