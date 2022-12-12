class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        maps = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        
        for i in range(len(num)):
            if not (num[i] in maps and maps[num[i]] == num[-1*i-1]):
                return False
            
        return True
