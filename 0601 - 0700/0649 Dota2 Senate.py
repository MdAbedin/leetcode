class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = deque(senate)
        radiants,dires = senate.count("R"),senate.count("D")
        r_bans,d_bans = 0,0

        while radiants and dires:
            if senate.popleft() == "R":
                if r_bans:
                    radiants -= 1
                    r_bans -= 1
                else:
                    d_bans += 1
                    senate.append("R")
            else:
                if d_bans:
                    dires -= 1
                    d_bans -= 1
                else:
                    r_bans += 1
                    senate.append("D")

        return "Radiant" if dires == 0 else "Dire"
