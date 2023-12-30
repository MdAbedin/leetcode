class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all(count%len(words) == 0 for count in Counter(chain(*words)).values())
