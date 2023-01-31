class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        data = sorted([age,score] for age,score in zip(ages,scores))
        dp = []
        
        for age,score in data:
            dp.append(max((total_score for (age2,score2),total_score in zip(data,dp) if age2 == age or score2 <= score), default = 0) + score)
            
        return max(dp)
