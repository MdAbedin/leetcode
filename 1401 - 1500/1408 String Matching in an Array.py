class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        
        for i in range(len(words)):
            found = False
            
            for j in range(len(words)):
                if i != j:
                    for k in range(len(words[j]) - len(words[i]) + 1):
                        matched = True
                        
                        for l in range(len(words[i])):
                            if words[j][k+l] != words[i][l]:
                                matched = False
                                break
                            
                        if matched:
                            ans.append(words[i])
                            found = True
                            break
                
                if found:
                    break
                    
        return ans
