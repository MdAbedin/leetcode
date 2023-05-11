class Solution:

    def romanToInt(self, s: str) -> int:

        values = {

            "I": 1,

            "V": 5,

            "X": 10,

            "L": 50,

            "C": 100,

            "D": 500,

            "M": 1000

        }

        

        ans = 0

        for i,c in enumerate(s):

            if i-1 >= 0 and values[s[i-1]] < values[c]: ans -= 2*values[s[i-1]]

            ans += values[c]

        return ans
