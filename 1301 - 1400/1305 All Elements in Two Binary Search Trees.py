# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def get_inorder_list(root):
    inorder_list = []
    stack = deque()
    cur = root

    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            inorder_list.append(cur.val)
            cur = cur.right
    
    return inorder_list

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        sorted1 = get_inorder_list(root1)
        sorted2 = get_inorder_list(root2)
        
        return merge(sorted1, sorted2)
