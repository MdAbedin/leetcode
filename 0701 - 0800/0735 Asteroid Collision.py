class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] > abs(asteroid):
                        break
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        break
                    else:
                        stack.pop()
                else:
                    stack.append(asteroid)

        return stack
