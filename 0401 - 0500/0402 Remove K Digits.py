class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        inds = defaultdict(deque)
        for i,d in enumerate(num): inds[d].append(i)

        ans = []
        next_ = 0

        for i in range(len(num)-k):
            for d in digits:
                while inds[d] and inds[d][0] < next_: inds[d].popleft()

                if inds[d] and inds[d][0] <= next_+k:
                    ans.append(d)
                    k -= inds[d][0]-next_
                    next_ = inds[d][0]+1
                    break

        return "0" if not (ans := "".join(ans).lstrip("0")) else ans
