"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        dct = {}
        dct[node] = Node(node.val)
        openl = deque([node])
        while openl:
            curr = openl.pop()
            for nei in curr.neighbors:
                if nei not in dct:
                    dct[nei] = Node(nei.val)
                    openl.append(nei)
                dct[curr].neighbors.append(dct[nei])
        return dct[node]