# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = []
        openl = deque([root])
        while openl:
            level = []
            for _ in range(len(openl)):
                curr = openl.popleft()
                if curr.left:
                    openl.append(curr.left)
                if curr.right:
                    openl.append(curr.right)
                level.append(curr.val)
            levels.append(level)
        rightSideView = []
        # print(levels)
        for level in levels:
            rightSideView.append(level[-1])
        return rightSideView