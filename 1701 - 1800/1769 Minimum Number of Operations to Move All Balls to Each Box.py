class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l,r = 0,boxes.count("1")
        m = sum(i for i,b in enumerate(boxes) if b == "1")
        ans = []

        for i,b in enumerate(boxes):
            ans.append(m)
            l += b == "1"
            r -= b == "1"
            m += l-r

        return ans
