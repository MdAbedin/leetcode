from sortedcontainers import SortedSet

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        servers_pq = [[weight,i] for i,weight in enumerate(servers)]
        heapify(servers_pq)
        tasks_queue = deque()
        ans = [None]*len(tasks)
        frees = defaultdict(list)
        times = SortedSet()

        for t,task in enumerate(tasks):
            times.discard(t)
            for server in frees[t]: heappush(servers_pq, server)
            tasks_queue.append([t,task])

            while servers_pq and tasks_queue:
                weight,server_i = heappop(servers_pq)
                t0,task = tasks_queue.popleft()
                ans[t0] = server_i
                frees[t + task].append([weight,server_i])
                times.add(t+task)

        while tasks_queue:
            t = times.pop(0)
            for server in frees[t]: heappush(servers_pq, server)

            while servers_pq and tasks_queue:
                weight,server_i = heappop(servers_pq)
                t0,task = tasks_queue.popleft()
                ans[t0] = server_i
                frees[t + task].append([weight,server_i])
                times.add(t+task)

        return ans
