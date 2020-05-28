class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        def helper(S, l, r):
            if r == l-1:
                return 0.5
            if r == l+1:
                return 1
            
            bal = 0
            for i in range(l,r+1):
                bal += 1 if S[i] == '(' else -1
                if bal == 0:
                    return 2*helper(S,l+1,i-1) + (helper(S,i+1,r) if i+1<r else 0)
                
        return int(helper(S, 0, len(S)-1))
