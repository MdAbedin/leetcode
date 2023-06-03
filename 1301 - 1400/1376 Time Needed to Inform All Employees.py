class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = defaultdict(list)
        for i,manager_id in enumerate(manager): subordinates[manager_id].append(i)

        def solve(ID):
            return informTime[ID] + max((solve(subordinate) for subordinate in subordinates[ID]), default=0)

        return solve(headID)
