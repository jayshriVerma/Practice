def findTilt(root: Optional[TreeNode]) -> int:
    total_tilt = 0
    
    def post_order(node):
        nonlocal total_tilt
        if not node:
            return 0
        
        left_sum = post_order(node.left)
        right_sum = post_order(node.right)
        
        # Calculate tilt for current node
        total_tilt += abs(left_sum - right_sum)
        
        # Return sum of values for this subtree
        return left_sum + right_sum + node.val
    
    post_order(root)
    return total_tilt

# here we use post-order traversal to calculate the sum of values for each subtree and the tilt for each node. The total tilt is accumulated in a nonlocal variable `total_tilt` which is returned at the end.
# Time Complexity: O(n) where n is the number of nodes in the tree, since we visit each node once.
    
# 563. binarytreetilt
# Given the root of a binary tree, return the sum of every tree node's tilt.
# The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. 
# If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.    
# Example 1:  
# Input: root = [1,2,3]
# Output: 1
# Explanation:
# Tilt of node 2 : |0-0| = 0 (no children)
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 1 : |2-3| = 1 (left subtree is node 2, right subtree is node 3)    