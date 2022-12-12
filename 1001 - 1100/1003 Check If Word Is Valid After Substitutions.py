class Solution:
    def isValid(self, S: str) -> bool:
        stack = deque()
        
        for char in S:
            if char == 'c':
                if len(stack) >= 2 and stack[-2] == 'a' and stack[-1] == 'b':
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        return not stack
