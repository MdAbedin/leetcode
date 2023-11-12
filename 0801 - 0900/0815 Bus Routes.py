class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        
        stop_to_routes = defaultdict(list)

        for i,route in enumerate(routes):
            for stop in route: stop_to_routes[stop].append(i)

        seen_routes = set(stop_to_routes[source])
        seen_stops = {stop for route in stop_to_routes[source] for stop in routes[route]}
        bfs = deque(seen_stops)
        d = 1

        while bfs:
            for i in range(len(bfs)):
                stop = bfs.popleft()
                if stop == target: return d

                for route in stop_to_routes[stop]:
                    if route in seen_routes: continue
                    seen_routes.add(route)

                    for stop in routes[route]:
                        if stop in seen_stops: continue
                        seen_stops.add(stop)
                        bfs.append(stop)

            d += 1

        return -1
