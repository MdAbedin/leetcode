class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        want = 1
        ans = []

        for num in target:
            if num != want: ans += ["Push"]*(num-want) + ["Pop"]*(num-want)
            ans.append("Push")
            want = num+1

        return ans
