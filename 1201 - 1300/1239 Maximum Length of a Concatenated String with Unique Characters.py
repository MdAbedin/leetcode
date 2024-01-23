class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return max(len("".join(subset)) for l in range(len(arr)+1) for subset in combinations(arr,l) if len(set("".join(subset))) == len("".join(subset)))
