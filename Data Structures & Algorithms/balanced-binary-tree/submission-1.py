class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs_height(node):
            if not node:
                return 0
            left = dfs_height(node.left)
            right = dfs_height(node.right)
            
            # If subtree is already unbalanced, propagate -1
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return dfs_height(root) != -1
