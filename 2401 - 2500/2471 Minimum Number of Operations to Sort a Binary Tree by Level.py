class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        bfs = [[root,0]]
        levels = defaultdict(list)

        for node,l in bfs:
            levels[l].append(node.val)

            for node2 in [node.left,node.right]:
                if not node2: continue
                bfs.append([node2,l+1])

        ans = 0

        for level in levels.values():
            inds = {v:i for i,v in enumerate(sorted(level))}

            for i in range(len(level)):
                while i != (i2:=inds[level[i]]):
                    level[i],level[i2] = level[i2],level[i]
                    ans += 1

        return ans
