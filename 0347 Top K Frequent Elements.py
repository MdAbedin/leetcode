class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      counts = Counter(nums)
      pq = []
      
      for num in counts:
        heappush(pq, (counts[num], num))
        if len(pq) == k+1: heappop(pq)
          
      return [heappop(pq)[1] for _ in range(len(pq))]
