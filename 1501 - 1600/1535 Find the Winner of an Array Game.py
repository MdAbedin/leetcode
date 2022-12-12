class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        nums = deque(arr)
        win_count = 0
        winner = nums[0]
        
        while True:
            a = nums.popleft()
            b = nums.popleft()
            if a > b:
                if winner == a:
                    win_count += 1
                    nums.append(b)
                    nums.appendleft(a)
                else:
                    winner = a
                    win_count = 1
                    nums.append(b)
                    nums.appendleft(a)
            else:
                if winner == b:
                    win_count += 1
                    nums.append(a)
                    nums.appendleft(b)
                else:
                    winner = b
                    win_count = 1
                    nums.append(a)
                    nums.appendleft(b)

            if win_count == k:
                return winner
            if win_count == len(arr)-1:
                return winner
