class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)

        while counts:
            if any(not counts[x] for x in range(min(counts),min(counts)+groupSize)): return False
            
            for x in range(min(counts),min(counts)+groupSize):
                counts[x] -= 1
                if not counts[x]: counts.pop(x)

        return True
