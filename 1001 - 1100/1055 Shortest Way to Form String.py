class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        leftmosts = defaultdict(lambda: -1)
        next_leftmosts = dict()
        
        for i in range(len(source)-1,-1,-1):
            next_leftmosts[i] = leftmosts.copy()
            leftmosts[source[i]] = i
            
        next_leftmosts[-1] = leftmosts
        cur = -1
        ans = 0
        
        for i in range(len(target)):
            if leftmosts[target[i]] == -1:
                return -1
            
            if next_leftmosts[cur][target[i]] == -1:
                ans += 1
                cur = -1
                
            cur = next_leftmosts[cur][target[i]]
            
        return ans+1
