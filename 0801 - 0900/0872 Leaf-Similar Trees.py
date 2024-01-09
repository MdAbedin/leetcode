class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_seqs = []

        for root in [root1,root2]:
            dfs = [root]
            leaf_seq = []

            while dfs:
                node = dfs.pop()
                if not node.left and not node.right: leaf_seq.append(node.val)
                if node.left: dfs.append(node.left)
                if node.right: dfs.append(node.right)

            leaf_seqs.append(leaf_seq)

        return leaf_seqs[0] == leaf_seqs[1]
