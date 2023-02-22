class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def works(capacity):
            capacity_left = 0
            days_used = 0

            for weight in weights:
                if weight > capacity: return False

                if weight > capacity_left:
                    days_used += 1
                    capacity_left = capacity - weight
                else:
                    capacity_left -= weight

            return days_used <= days

        return bisect_left(range(sum(weights)+1), True, key = works)
