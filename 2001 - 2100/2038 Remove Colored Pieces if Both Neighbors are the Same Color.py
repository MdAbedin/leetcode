class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        return sum(max(0,len(list(g))-2) for k,g in groupby(colors) if k == "A") > sum(max(0,len(list(g))-2) for k,g in groupby(colors) if k == "B")
