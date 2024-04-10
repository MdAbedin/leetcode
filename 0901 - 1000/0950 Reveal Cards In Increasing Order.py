class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = deque()

        for num in sorted(deck,reverse=True):
            if ans: ans.appendleft(ans.pop())
            ans.appendleft(num)

        return ans
