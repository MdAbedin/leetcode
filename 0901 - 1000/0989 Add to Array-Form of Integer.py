class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return map(int,str(int("".join(map(str,num))) + k))
