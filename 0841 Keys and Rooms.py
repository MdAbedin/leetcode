class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set([0])
        bfs = deque([0])
        
        while bfs:
            cur = bfs.popleft()
            
            for room in rooms[cur]:
                if room not in seen:
                    seen.add(room)
                    bfs.append(room)
        
        return len(seen) == len(rooms)
