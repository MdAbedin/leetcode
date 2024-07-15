class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = defaultdict(lambda: [None,None])
        root = {node for *nodes,_ in descriptions for node in nodes}

        for p,c,l in descriptions:
            children[p][not l] = c
            root.discard(c)

        def solve(node): return None if not node else TreeNode(node,*map(solve,children[node]))

        return solve(next(iter(root)))
