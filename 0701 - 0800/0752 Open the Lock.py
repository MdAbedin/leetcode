class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends: return -1
        
        seen = {"0000"}
        bfs = [("0000",0)]

        for lock,turns in bfs:
            if lock == target: return turns

            for i,d in enumerate(lock):
                for diff in [-1,1]:
                    lock2 = lock[:i]+str((int(d)+diff)%10)+lock[i+1:]
                    if lock2 in deadends or lock2 in seen: continue
                    seen.add(lock2)
                    bfs.append((lock2,turns+1))

        return -1
