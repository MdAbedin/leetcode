class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0

        for k,g in groupby(s,key="ab".__contains__):
            if not k: continue
            
            g = list(g)
            cur_ans = 0

            for sub,p1,p2 in [[["a","b"],x,y],[["b","a"],y,x]]:
                stack = []
                cur_ans2 = 0

                for c in g:
                    stack.append(c)

                    if stack[-2:] == sub:
                        stack.pop()
                        stack.pop()
                        cur_ans2 += p1

                cur_ans = max(cur_ans,cur_ans2+p2*min(stack.count("a"),stack.count("b")))

            ans += cur_ans

        return ans
