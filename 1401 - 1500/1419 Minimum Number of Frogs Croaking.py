class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = cur_frogs = c = r = o = a = k = 0
        
        for i in range(len(croakOfFrogs)-1,-1,-1):
            char = croakOfFrogs[i]
            
            if char == 'c':
                c += 1
                cur_frogs -= 1
            elif char == 'r':
                r += 1
            elif char == 'o':
                o += 1
            elif char == 'a':
                a += 1
            elif char == 'k':
                k += 1
                cur_frogs += 1
            else:
                return -1

            ans = max(ans, cur_frogs)
            
            if c > r or r > o or o > a or a > k:
                return -1
            
        return ans
