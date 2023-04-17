class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [all(candies[i]+extraCandies >= candies[j] for j in range(len(candies)) if i != j) for i in range(len(candies))]
