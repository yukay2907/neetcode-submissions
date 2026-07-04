# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxi):
            if not node:
                return 0
            if node.val >= maxi:
                good = 1
                maxi = node.val
            else:
                good = 0
            return good + dfs(node.left,maxi) + dfs(node.right,maxi)
        return dfs(root,float('-inf'))