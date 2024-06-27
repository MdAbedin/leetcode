class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return Counter(chain(*edges)).most_common(1)[0][0]
