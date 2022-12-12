class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        sh,sm = map(int, startTime.split(":"))
        fh,fm = map(int, finishTime.split(":"))
        
        if fh < sh or (fh == sh and fm < sm):
            return self.numberOfRounds(startTime, "24:00") + self.numberOfRounds("00:00", finishTime)
        else:
            mid = max(0,fh-sh-1)*4
            s = 0 if sm > 45 else (1 if sm > 30 else (2 if sm > 15 else (3 if sm > 0 else 4)))
            f = 0 if fm < 15 else (1 if fm < 30 else (2 if fm < 45 else 3))
            if sh == fh:
                qs = [1 if s >= 4-i and f >= i+1 else 0 for i in range(4)]
                return mid + sum(qs)
            else:
                return mid + s + f
