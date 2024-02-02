class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for d in range(1,10): ans += [num*10+d for num in ans if num%10 == d-1] + [d]
        return [num for num in sorted(ans) if low <= num <= high]
