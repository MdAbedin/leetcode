class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]: return "0"

        results = []

        for i in range(len(num2)):
            results.append([0]*i)
            carry = 0

            for digit in reversed(num1):
                carry,result = divmod(int(num2[~i])*int(digit)+carry,10)
                results[-1].append(result)

            if carry: results[-1].append(carry)

        ans = []
        carry = 0

        for i in range(len(results[-1])):
            carry,result = divmod(sum(result[i] if i < len(result) else 0 for result in results)+carry,10)
            ans.append(result)

        if carry: ans.append(carry)

        return "".join(map(str,reversed(ans)))
