class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)

        for a,b in roads:
            graph[a].append(b)
            graph[b].append(a)

        def solve(node,parent):
            empty_seats,cars,fuel = 0,0,0

            for node2 in graph[node]:
                if node2 != parent:
                    empty_seats2,cars2,fuel2 = solve(node2,node)
                    empty_seats += empty_seats2
                    cars += cars2
                    fuel += fuel2 + cars2

            if empty_seats == 0:
                cars += 1
                empty_seats = seats-1
            else:
                empty_seats -= 1
                cars_to_remove = empty_seats // seats
                cars -= cars_to_remove
                empty_seats -= cars_to_remove * seats

            return empty_seats,cars,fuel

        return solve(0,None)[2]
