class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secret_knowers = {0,firstPerson}
        time_to_meetings = defaultdict(list)
        for x,y,t in meetings: time_to_meetings[t].append((x,y))

        for t,meetings in sorted(time_to_meetings.items()):
            g = defaultdict(set)
            seen = set()

            for x,y in meetings:
                g[x].add(y)
                g[y].add(x)
                if x in secret_knowers: seen.add(x)
                if y in secret_knowers: seen.add(y)

            bfs = list(seen)

            for p in bfs:
                for p2 in g[p]:
                    if p2 in seen: continue
                    
                    seen.add(p2)
                    secret_knowers.add(p2)
                    bfs.append(p2)

        return secret_knowers
