class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nums = []

        def iot(node):
            if not node: return
            iot(node.left)
            nums.append(node.val)
            iot(node.right)

        iot(root)

        swapped = []

        smaller = None

        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]: smaller = nums[i]

        swapped.append(smaller)
        bigger = None

        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]: bigger = nums[i]

        swapped.append(bigger)

        dfs = [root]

        while dfs:
            node = dfs.pop()

            if node.val == swapped[0]: node.val = swapped[1]
            elif node.val == swapped[1]: node.val = swapped[0]

            if node.left: dfs.append(node.left)
            if node.right: dfs.append(node.right)