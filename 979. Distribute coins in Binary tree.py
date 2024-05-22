from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            self.moves += abs(left_excess) + abs(right_excess)
            return node.val + left_excess + right_excess - 1
        self.moves = 0
        dfs(root)
        return self.moves
# Example 1:
root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)
sol = Solution()
print(sol.distributeCoins(root))  # Output will be: 2
# Example 2:
root = TreeNode(0)
root.left = TreeNode(3)
root.right = TreeNode(0)
print(sol.distributeCoins(root))  # Output will be: 3
