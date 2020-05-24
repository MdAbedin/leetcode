# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        ans = 0
        
        stack = deque([root])
        counts = defaultdict(int)
        seen = set()
        
        while stack:
            cur = stack[-1]
            
            if cur in seen:
                stack.pop()
                counts[cur.val] -= 1
                continue
            else:
                counts[cur.val] += 1
                seen.add(cur)
            
            if not cur.left and not cur.right:
                ans += 1 if (sum(counts[key]%2 for key in range(1,10)) <= 1) else 0
                counts[cur.val] -= 1
                stack.pop()
            else:
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)

        return ans
