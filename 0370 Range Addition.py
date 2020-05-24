class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        changes = [[0,0] for i in range(length)]
        
        for start, end, change in updates:
            changes[start][0] += change
            changes[end][1] += change
            
        ans = [0]*length
        
        for i in range(length):
            ans[i] = (ans[i-1] if i-1 >= 0 else 0) + changes[i][0] - (changes[i-1][1] if i-1>=0 else 0)
            
        return ans
