class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return deepcopy(node)
