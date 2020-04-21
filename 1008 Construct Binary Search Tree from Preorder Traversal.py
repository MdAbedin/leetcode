# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        parents_and_ranges = deque()
        parents_and_ranges.append([root, None, None])
        parent, less_than, greater_than = parents_and_ranges[-1]
        
        for i in range(1,len(preorder)):
            parent, less_than, greater_than = parents_and_ranges[-1]

            cur_val = preorder[i]
            cur_node = TreeNode(cur_val)

            while not ((less_than is None or cur_val < less_than) and (greater_than is None or cur_val > greater_than)):
                parents_and_ranges.pop()
                parent, less_than, greater_than = parents_and_ranges[-1]
            
            if cur_val < parent.val:
                parent.left = cur_node
                parents_and_ranges.append([cur_node, min(parent.val if less_than is None else less_than , parent.val), greater_than])
            else:
                parent.right = cur_node
                parents_and_ranges.append([cur_node, less_than, max(parent.val if greater_than is None else greater_than, parent.val)])

        return root
