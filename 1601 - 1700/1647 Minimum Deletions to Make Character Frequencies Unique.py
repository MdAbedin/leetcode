class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = [0]*(len(s)+1)
        for freq in Counter(s).values(): freqs[freq] += 1
        ans = 0

        for i in range(len(freqs)-1,0,-1):
            ans += max(0,freqs[i]-1)
            freqs[i-1] += max(0,freqs[i]-1)

        return ans
