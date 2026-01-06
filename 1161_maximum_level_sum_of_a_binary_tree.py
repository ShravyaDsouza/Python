# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sums = []

        def dfs(node, level):
            if not node:
                return
            if level == len(level_sums):
                level_sums.append(node.val)
            else:
                level_sums[level] += node.val
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
        dfs(root, 0)
    
        max_sum = max(level_sums)
        for i, s in enumerate(level_sums):
            if s == max_sum:
                return i + 1
