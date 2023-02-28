class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        representations = defaultdict(list)

        def helper(node):
            if not node: return None
            
            representation = (node.val, helper(node.left), helper(node.right))
            representations[representation].append(node)
            
            return representation

        helper(root)

        return [nodes[0] for nodes in representations.values() if len(nodes) >= 2]
