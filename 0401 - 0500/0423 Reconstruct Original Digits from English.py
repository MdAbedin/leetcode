class Solution:
    def originalDigits(self, s: str) -> str:
        spellings = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
        maps = [('w',2), ('u', 4), ('z', 0), ('x', 6), ('g', 8), ('o', 1), ('r', 3), ('f', 5), ('v', 7), ('i', 9)]
        char_counts = defaultdict(int)
        ans_counts = defaultdict(int)
        
        for char in s:
            char_counts[char] += 1
            
        for char, digit in maps:
            ans_counts[digit] = count = char_counts[char]
            
            for char2 in spellings[digit]:
                char_counts[char2] -= count
        
        ans = ''
        
        for digit in sorted(ans_counts.keys()):
            ans += str(digit)*ans_counts[digit]
            
        return ans
