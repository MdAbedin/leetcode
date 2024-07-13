class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        ans = {}
        stack = []
        
        for p,h,d in sorted(map(list,zip(positions,healths,directions))):
            if d == "R":
                stack.append([p,h])
            else:
                while stack:
                    if stack[-1][1] < h:
                        stack.pop()
                        h -= 1
                    elif stack[-1][1] == h:
                        stack.pop()
                        h = 0
                        break
                    else:
                        stack[-1][1] -= 1
                        h = 0
                        break
                        
                if h > 0: ans[p] = h
            
        for p,h in stack: ans[p] = h
        
        return [ans[p] for p in positions if p in ans]
