class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        
        @cache
        def works(s):
            return any(s[:i] in words and (s[i:] in words or works(s[i:])) for i in range(1,len(s)))
        
        return filter(works, words)
