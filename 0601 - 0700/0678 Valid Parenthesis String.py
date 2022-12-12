class Solution:
    def checkValidString(self, s: str) -> bool:
        least_opens = most_opens = 0
        
        for char in s:
            least_opens += 1 if char == '(' else -1
            most_opens += -1 if char == ')' else 1
            least_opens = max(least_opens, 0)
            
            if most_opens < 0:
                return 0

        return least_opens == 0
