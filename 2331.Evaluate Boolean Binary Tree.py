from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val in [0, 1]:
            return bool(root.val)
        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)
        if root.val == 2:
            return left_result or right_result
        elif root.val == 3:
            return left_result and right_result
        else:
            return False

# 1st and 2nd test case:
solution = Solution()
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
root1.right.left = TreeNode(0)
root1.right.right = TreeNode(1)
print(solution.evaluateTree(root1))  #For 1st test case Output will be True

root2 = TreeNode(0)
print(solution.evaluateTree(root2))  # for second test case Output will be False

