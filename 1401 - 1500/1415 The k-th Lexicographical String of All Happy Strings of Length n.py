class Solution:
    def is_happy(self, s):
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return False
            
        return True
    
    def getHappyString(self, n: int, k: int) -> str:
        all_strings = ['']
        
        while len(all_strings) < 3**n:
            for i in range(len(all_strings)):
                all_strings.append(all_strings[i]+'b')
                all_strings.append(all_strings[i]+'c')
                all_strings[i] += 'a'
                
        all_strings.sort()
        
        for string in all_strings:
            if self.is_happy(string):
                k -= 1
                if k == 0:
                    return string
        
        return ''
