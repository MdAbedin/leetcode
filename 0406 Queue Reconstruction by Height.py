class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = [0]*len(people)
        people.sort()
        last_height, i, taller_before_ctr = -1, 0, -1
        
        for height, taller_before in people:
            if height != last_height: i, taller_before_ctr = 0, -1
                
            while taller_before_ctr != taller_before:
                if not ans[i]: taller_before_ctr += 1
                i += 1
                
            ans[i-1] = [height, taller_before]
            last_height = height
        
        return ans
