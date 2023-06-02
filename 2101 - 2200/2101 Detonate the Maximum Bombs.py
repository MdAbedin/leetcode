class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ans = 1

        for start_i in range(len(bombs)):
            dfs = [start_i]
            used = {start_i}
            cur_ans = 1

            while dfs:
                i = dfs.pop()
                x,y,r = bombs[i]

                for j,(x2,y2,r2) in enumerate(bombs):
                    if j not in used and dist([x,y],[x2,y2]) <= r:
                        used.add(j)
                        dfs.append(j)
                        cur_ans += 1

            ans = max(ans,cur_ans)

        return ans
