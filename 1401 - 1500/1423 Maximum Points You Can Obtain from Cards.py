class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_sum = sum(cardPoints[:k])
        cur_sum = max_sum
        
        for i in range(k):
            cur_sum = cur_sum - cardPoints[k-1-i] + cardPoints[-1*i-1]
            max_sum = max(max_sum, cur_sum)
            
        return max_sum
