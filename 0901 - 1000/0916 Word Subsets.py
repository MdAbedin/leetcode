class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans = []
        B_counts = defaultdict(int)
        
        for word in B:
            word_counts = defaultdict(int)
            
            for char in word:
                word_counts[char] += 1
                
            for char in word_counts:
                B_counts[char] = max(B_counts[char], word_counts[char])
        
        for word in A:
            word_counts = defaultdict(int)
            
            for char in word:
                word_counts[char] += 1
                
            is_universal = True
            for char in B_counts:
                if word_counts[char] < B_counts[char]:
                    is_universal = False
                    break
                
            if is_universal:
                ans.append(word)
                
        return ans
