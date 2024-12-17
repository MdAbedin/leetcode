class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = sorted([-ord(char),count] for char,count in Counter(s).items())
        ans = []
        
        while pq:
            neg_ord,count = heappop(pq)
            c = chr(-neg_ord)
            
            if ans and c == ans[-1][0]:
                if ans[-1][1] == repeatLimit:
                    if not pq: break
                    ans.append([chr(-pq[0][0]),1])
                    pq[0][1] -= 1
                    if pq[0][1] == 0: heappop(pq)
                    heappush(pq,[neg_ord,count])
                else:
                    ans[-1][1] += 1
                    if count-1 != 0: heappush(pq,[neg_ord,count-1])
            else:
                ans.append([c,1])
                if count-1 != 0: heappush(pq,[neg_ord,count-1])
        
        return "".join(ch*c for ch,c in ans)
