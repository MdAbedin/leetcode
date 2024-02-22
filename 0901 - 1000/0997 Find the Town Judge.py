class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ins,outs = [0]*n,[0]*n

        for a,b in trust:
            ins[b-1] += 1
            outs[a-1] += 1

        judges = [i for i in range(n) if ins[i] == n-1 and outs[i] == 0]

        return -1 if len(judges) != 1 else judges[0]+1
