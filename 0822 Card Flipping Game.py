class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        all_nums = set()
        both_sides_nums = set()
        
        for i in range(len(fronts)):
            all_nums.add(fronts[i])
            all_nums.add(backs[i])
            
            if fronts[i] == backs[i]:
                both_sides_nums.add(fronts[i])
                
        candidates = all_nums - both_sides_nums
        return min(candidates) if candidates else 0
