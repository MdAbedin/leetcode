class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        
        counts = Counter(tasks)
        max_count = max(counts[c] for c in counts)
        num_max = sum(1 if counts[c] == max_count else 0 for c in counts)
        
        if (max_count-1)*(n+1)+1+num_max-1 >= len(tasks): return (max_count-1)*(n+1)+1+num_max-1
        return len(tasks)
