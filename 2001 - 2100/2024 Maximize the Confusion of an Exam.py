class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        idxs = defaultdict(list)
        for i,a in enumerate(answerKey): idxs[a].append(i)

        ti,fi = 0,0
        ans = 0

        for i in range(len(answerKey)):
            while ti < len(idxs["T"]) and idxs["T"][ti] < i: ti += 1
            while fi < len(idxs["F"]) and idxs["F"][fi] < i: fi += 1

            ans = max(ans, max(len(answerKey) if ti+k >= len(idxs["T"]) else idxs["T"][ti+k], len(answerKey) if fi+k >= len(idxs["F"]) else idxs["F"][fi+k])-i)

        return ans
