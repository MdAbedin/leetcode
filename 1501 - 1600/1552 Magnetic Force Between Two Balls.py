class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def fails(f):
            c,p = 0,-inf

            for x in position:
                if x-p >= f:
                    c += 1
                    p = x

            return c < m

        return bisect_left(range(10**9),True,key=fails)-1
