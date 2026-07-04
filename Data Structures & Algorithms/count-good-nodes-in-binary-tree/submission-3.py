# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node,maxi):
            if not node:
                return
            if node.val >= maxi:
                self.count += 1
                maxi = node.val
            dfs(node.left,maxi)
            dfs(node.right,maxi)
        dfs(root,float('-inf'))
        return self.count