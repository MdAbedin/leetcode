class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        i = 0

        while i < len(s):
            if s[i].isalpha():
                ans.append(s[i])
            else:
                open_i = s.index("[",i)
                k = int(s[i:open_i])
                level = 1
                for j in range(open_i+1,len(s)):
                    if s[j] == "[": level += 1
                    if s[j] == "]": level -= 1
                    if level == 0:
                        close_i = j
                        break
                encoded = s[open_i+1:close_i]
                ans.append(self.decodeString(encoded)*k)
                i = close_i

            i += 1

        return "".join(ans)
