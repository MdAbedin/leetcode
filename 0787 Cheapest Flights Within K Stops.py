class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for a,b,price in flights:
            graph[a].append([b,price])
        
        bests = defaultdict(lambda: inf)
        bfs = deque([[src,0]])
        
        for i in range(k+1):
            for j in range(len(bfs)):
                cur,total_price = bfs.popleft()

                for city,price in graph[cur]:
                    if total_price + price < bests[city]:
                        bests[city] = total_price + price
                        bfs.append([city,total_price + price])
                    
        return -1 if bests[dst] == inf else bests[dst]
