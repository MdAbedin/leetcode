class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter(map(tuple,grid))
        col_counts = Counter(map(tuple,zip(*grid)))

        return sum(row_counts[vals]*col_counts[vals] for vals in row_counts)
