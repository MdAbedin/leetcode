class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        min_sum = sum(floor(float(price)) for price in prices)
        if min_sum > target: return "-1"

        ceil_diffs = [ceil(float(price)) - float(price) for price in prices if floor(float(price)) != ceil(float(price))]
        if len(ceil_diffs) < target - min_sum: return "-1"

        return "{:.3f}".format(sum(float(price) - floor(float(price)) for price in prices) + sum(2*x-1 for x in sorted(ceil_diffs)[:target - min_sum]))
