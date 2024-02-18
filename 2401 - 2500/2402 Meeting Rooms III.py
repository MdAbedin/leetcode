from sortedcontainers import SortedList

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counts = [0]*n
        events = SortedList([[s,"start",e] for s,e in meetings])
        pending = deque()
        rooms = list(range(n))

        while events:
            match events.pop(0):
                case [t,"start",e]: pending.append(e-t)
                case [t,"end",room]: heappush(rooms,room)

            while pending and rooms:
                room,d = heappop(rooms),pending.popleft()
                counts[room] += 1
                events.add([t+d,"end",room])

        return max(range(n),key=counts.__getitem__)
