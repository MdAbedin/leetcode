
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def iot(node): return [] if not node else iot(node.left) + [node.val] + iot(node.right)
        self.iterator = iter(iot(root))

    def next(self) -> int:
        return next(self.iterator)

    def hasNext(self) -> bool:
        return self.iterator.__length_hint__() > 0
