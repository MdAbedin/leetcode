class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        counts = Counter()
        ans = 0

        for end in range(len(fruits)):
            counts[fruits[end]] += 1
            
            while len(counts) > 2:
                counts[fruits[start]] -= 1
                if counts[fruits[start]] == 0: counts.pop(fruits[start])
                start += 1

            ans = max(ans, end-start+1)

        return ans
