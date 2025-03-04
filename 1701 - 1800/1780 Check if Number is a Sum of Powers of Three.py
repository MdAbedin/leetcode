class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n%3 == 2: return False
            n //= 3

        return True
