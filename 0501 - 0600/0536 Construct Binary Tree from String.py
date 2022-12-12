# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, l, r):
        if l >= r: return TreeNode(int(self.s[l])) if l==r else None
        
        bal = 0
        i = l+1
        
        while True:
            if self.s[i] == '(': bal += 1
            if self.s[i] == ')': bal -= 1
            if bal == 0: break
            i += 1
            
        return TreeNode(int(self.s[l]), self.helper(l+2, i-1), self.helper(i+2, r-1))
    
    def str2tree(self, s: str) -> TreeNode:
        new_s = []
        cur = ''
        
        for i in range(len(s)):
            if s[i] == '(' or s[i] == ')':
                if cur:
                    new_s.append(cur)
                    cur = ''
                new_s.append(s[i])
            else:
                cur += s[i]
        if cur: new_s.append(cur)
            
        self.s = new_s
        
        return self.helper(0, len(self.s)-1)
