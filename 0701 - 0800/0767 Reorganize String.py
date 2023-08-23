class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        pq = [(-count,c) for c,count in Counter(s).items()]
        heapify(pq)

        while pq:
            count,c = heappop(pq)
            count *= -1

            if ans and ans[-1] == c:
                if not pq: return ""

                count2,c2 = heappop(pq)
                count2 *= -1

                ans.append(c2)
                if count2-1 >= 1: heappush(pq,(-(count2-1),c2))
                heappush(pq,(-count,c))
            else:
                ans.append(c)
                if count-1 >= 1: heappush(pq,(-(count-1),c))

        return "".join(ans)
