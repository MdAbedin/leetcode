class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        pairs1 = {(0,0)}
        for rod in rods[:len(rods)//2]: pairs1 = {new_pair for h1,h2 in pairs1 for new_pair in [(h1,h2),(h1+rod,h2),(h1,h2+rod)]}

        pairs2 = {(0,0)}
        for rod in rods[len(rods)//2:]: pairs2 = {new_pair for h1,h2 in pairs2 for new_pair in [(h1,h2),(h1+rod,h2),(h1,h2+rod)]}

        diff_max_heights1 = defaultdict(int)
        for h1,h2 in pairs1: diff_max_heights1[h1-h2] = max(diff_max_heights1[h1-h2],h1)

        return max((h1+diff_max_heights1[-(h1-h2)] for h1,h2 in pairs2 if -(h1-h2) in diff_max_heights1), default = 0)
