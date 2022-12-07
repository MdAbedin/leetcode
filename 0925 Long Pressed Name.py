class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def groups(string): return [[char, len(list(group))] for char, group in groupby(string)]
        
        groups1, groups2 = groups(name), groups(typed)

        return len(groups1) == len(groups2) and all(char1 == char2 and len1 <= len2 for (char1, len1), (char2, len2) in zip(groups1, groups2))
