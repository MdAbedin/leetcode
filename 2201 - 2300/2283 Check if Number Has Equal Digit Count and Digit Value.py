class Solution:
    def digitCount(self, num: str) -> bool:
        return all(num.count(str(i)) == int(num[i]) for i in range(len(num)))
