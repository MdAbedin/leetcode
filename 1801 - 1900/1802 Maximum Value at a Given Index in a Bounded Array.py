class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def fails(x):
            s = x

            for d in [index,n-1-index]:
                low = max(1,x-d)
                s += (x-1)*x//2 - (low-1)*low//2
                if d >= x: s += d-x+1

            return s > maxSum

        return bisect_left(range(maxSum+1),True,key=fails)-1
