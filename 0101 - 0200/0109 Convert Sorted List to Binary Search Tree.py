class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        def solve(l,r):
            if l > r: return None
            m = (l+r)//2
            return TreeNode(values[m], solve(l,m-1), solve(m+1,r))

        return solve(0,len(values)-1)
