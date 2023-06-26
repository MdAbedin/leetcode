class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        used = set()
        pq = []

        for i in range(candidates):
            if i not in used:
                used.add(i)
                heappush(pq, [costs[i],i,True])

            back_i = len(costs)-1-i

            if back_i not in used:
                used.add(back_i)
                heappush(pq, [costs[back_i],back_i,False])

        front_i = candidates
        back_i = len(costs)-1-candidates
        ans = 0

        for i in range(k):
            cost,j,front = heappop(pq)
            ans += cost

            if front:
                if front_i < len(costs) and front_i not in used:
                    used.add(front_i)
                    heappush(pq, [costs[front_i],front_i,True])
                    front_i += 1
            else:
                if back_i >= 0 and back_i not in used:
                    used.add(back_i)
                    heappush(pq, [costs[back_i],back_i,False])
                    back_i -= 1

        return ans
