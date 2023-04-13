class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed,popped = deque(pushed),deque(popped)
        stack = []
        
        while popped:
            while pushed and (not stack or stack[-1] != popped[0]): stack.append(pushed.popleft())
            if stack[-1] != popped[0]: return False
            stack.pop()
            popped.popleft()

        return True
