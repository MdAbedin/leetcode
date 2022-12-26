class Solution:

    def takeCharacters(self, s: str, k: int) -> int:

        d = defaultdict(lambda: {0:-1})

        for i,c in enumerate(s): d[c][len(d[c])] = i

            

        counts = defaultdict(int)

        ans = inf

        

        for i in range(len(s),-1,-1):

            if i != len(s): counts[s[i]] += 1

            

            a_need = max(0,k-counts["a"])

            b_need = max(0,k-counts["b"])

            c_need = max(0,k-counts["c"])

            

            ia = d["a"].get(a_need,None)

            ib = d["b"].get(b_need,None)

            ic = d["c"].get(c_need,None)

            

            if None in [ia,ib,ic] or max(ia,ib,ic) >= i: break

                

            ans = min(ans, len(s)-i + max(ia,ib,ic)+1)

                

        return -1 if ans == inf else ans
