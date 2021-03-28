class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        ans = []
        maps = dict(knowledge)
        l = 0
        key = []
        
        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            elif s[i] == ")":
                str_key = "".join(key)
                ans.append(maps[str_key] if str_key in maps else "?")
                key = []
                l -= 1
            else:
                if l == 1:
                    key.append(s[i])
                else:
                    ans.append(s[i])
                    
        return "".join(ans)
