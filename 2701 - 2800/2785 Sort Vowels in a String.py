class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_inds = [i for i,c in enumerate(s) if c.lower() in "aeiou"]
        vowels = [c for i,c in enumerate(s) if c.lower() in "aeiou"]
        vowels.sort()
        consonants = [[c,i] for i,c in enumerate(s) if c.lower() not in "aeiou"]
        ans = [""]*len(s)
        
        for i,c in zip(vowel_inds,vowels): ans[i] = c
        for c,i in consonants: ans[i] = c
            
        return "".join(ans)
