class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        r = list(zip(reward1,reward2))
        r.sort(key = lambda pair: pair[0]-pair[1] ,reverse=True)
        return sum(r[i][0] for i in range(k)) + sum(r[i][1] for i in range(k,len(r)))
