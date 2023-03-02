class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []

        for char,group in groupby(chars):
            ans += [char]
            length = len(list(group))
            if length > 1: ans += list(str(length))

        chars[:] = ans

        return len(ans)
