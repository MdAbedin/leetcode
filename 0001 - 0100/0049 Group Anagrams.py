class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return reduce(lambda d,s: d[tuple(sorted(s))].append(s) or d,strs,defaultdict(list)).values()
