class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []

        def get_subtree_sum(node):
            if not node:
                return 0
            
            # Postorder: Left -> Right -> Node
            left_sum = get_subtree_sum(node.left)
            right_sum = get_subtree_sum(node.right)
            
            current_sum = node.val + left_sum + right_sum
            all_sums.append(current_sum)
            return current_sum

        total_sum = get_subtree_sum(root)
        
        max_prod = 0
        for s in all_sums:
            product = s * (total_sum - s)
            if product > max_prod:
                max_prod = product
        
        return max_prod % (10**9 + 7)
