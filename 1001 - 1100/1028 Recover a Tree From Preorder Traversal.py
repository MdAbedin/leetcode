class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        groups = [list(g) for k,g in groupby(traversal,key = lambda c: c == "-")]
        nodes = {0:TreeNode(int("".join(groups[0])))}

        for i in range(1,len(groups),2):
            d = len(list(groups[i]))
            v = int("".join(groups[i+1]))
            nodes[d] = TreeNode(v)
            
            if not nodes[d-1].left: nodes[d-1].left = nodes[d]
            else: nodes[d-1].right = nodes[d]

        return nodes[0]
