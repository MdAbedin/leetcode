class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect_right(letters,target)
        return letters[0] if i == len(letters) else letters[i]
