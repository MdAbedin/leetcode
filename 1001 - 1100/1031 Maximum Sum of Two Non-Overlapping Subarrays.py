class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        psums = [0] + list(accumulate(nums))
        first_len_max = -inf
        second_len_max = -inf
        ans = -inf

        for i in range(firstLen + secondLen, len(psums)):
            first_len_max = max(first_len_max, psums[i - secondLen] - psums[i - secondLen - firstLen])
            second_len_max = max(second_len_max, psums[i - firstLen] - psums[i - firstLen - secondLen])
            ans = max(ans, psums[i] - psums[i - firstLen] + second_len_max, psums[i] - psums[i - secondLen] + first_len_max)

        return ans
