class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        ans = 0
        counts = Counter()
        consonants = 0
        i2 = i3 = i4 = 0

        for i1 in range(len(word)):
            while i2 < len(word) and consonants < k:
                consonants += word[i2] not in "aeiou"
                i2 += 1

            while i3 < len(word) and len(counts) < 5:
                if word[i3] in "aeiou": counts[word[i3]] += 1
                i3 += 1

            i4 = max(i4,i2)
            while i4 < len(word) and word[i4] in "aeiou": i4 += 1

            if consonants == k and len(counts) == 5 and i3 <= i4: ans += i4-max(i2,i3)+1

            consonants -= word[i1] not in "aeiou"
            
            if word[i1] in "aeiou":
                counts[word[i1]] -= 1
                if counts[word[i1]] == 0: counts.pop(word[i1])

        return ans
