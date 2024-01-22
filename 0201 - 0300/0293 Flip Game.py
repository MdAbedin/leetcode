class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        return [currentState[:i]+"--"+currentState[i+2:] for i in range(len(currentState)) if currentState.startswith("++",i)]
