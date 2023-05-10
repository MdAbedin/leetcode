class Solution:
    def intToRoman(self, num: int) -> str:
        ones = "IXCM"
        fives = "VLD"
        num_str = str(num)
        ans = []

        for i in range(len(num_str)):
            digit = int(num_str[~i])

            if 1 <= digit <= 3:
                ans.append(ones[i]*digit)
            elif digit == 4:
                ans.append(ones[i] + fives[i])
            elif 5 <= digit <= 8:
                ans.append(fives[i] + (digit-5)*ones[i])
            elif digit == 9:
                ans.append(ones[i] + ones[i+1])

        return "".join(ans[::-1])
