class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum((ord(c)-ord("A")+1)*26**i for i,c in enumerate(columnTitle[::-1]))
