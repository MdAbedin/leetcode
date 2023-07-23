class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        ans = [[None]]

        for size in range(1,n+1):
            if size%2 == 0:
                ans.append([])
                continue
                
            cur_ans = []

            for l_size in range(size):
                for l_tree in ans[l_size]:
                    for r_tree in ans[size-1-l_size]:
                        cur_ans.append(TreeNode(0,l_tree,r_tree))

            ans.append(cur_ans)

        return ans[n]
