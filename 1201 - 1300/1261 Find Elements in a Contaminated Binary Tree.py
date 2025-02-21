class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.nums = set()
        bfs = [[root,0]]

        for node,x in bfs:
            self.nums.add(x)

            if node.left: bfs.append([node.left,2*x+1])
            if node.right: bfs.append([node.right,2*x+2])

    def find(self, target: int) -> bool:
        return target in self.nums
