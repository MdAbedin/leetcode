class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        for a,b in edges: neighbors[a].append(b)

        seen = set()

        def has_cycle(node,path):
            if node in seen: return False
            
            seen.add(node)
            path.add(node)

            for neighbor in neighbors[node]:
                if neighbor in path or has_cycle(neighbor,path): return True

            path.remove(node)

            return False

        if any(has_cycle(node,set()) for node in range(len(colors))): return -1

        @cache
        def solve(node,color):
            return (colors[node] == color) + max((solve(neighbor,color) for neighbor in neighbors[node]), default = 0)

        return max(solve(node,color) for color in set(colors) for node in range(len(colors)))
