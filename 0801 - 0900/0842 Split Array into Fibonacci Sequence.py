class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def is_valid(s): return int(s) < 2**31 and (s == "0" or s[0] != "0")

        for i in range(1,len(num)):
            num1 = num[:i]
            if not is_valid(num1): continue

            for j in range(i+1,len(num)):
                num2 = num[i:j]
                if not is_valid(num2): continue

                ans = [int(num1),int(num2)]
                index = j

                while index < len(num):
                    next_num = ans[-2]+ans[-1]
                    if not(next_num < 2**31 and num.startswith(str(next_num),index)): break
                    ans.append(next_num)
                    index += len(str(next_num))

                if index == len(num): return ans

        return []
