def largestBSTSubtree(root):
        max_size = 0
        
        def dfs(node):
            nonlocal max_size
            if not node:
                return True, 0, float('inf'), float('-inf')
            
            left_is_bst, left_size, left_min, left_max = dfs(node.left)
            right_is_bst, right_size, right_min, right_max = dfs(node.right)
            
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                size = left_size + right_size + 1
                max_size = max(max_size, size)
                
                return True, size, min(left_min, node.val), max(right_max, node.val)
            
            return False, 0, 0, 0  # invalid BST
        
        dfs(root)
        return max_size

# Example usage:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    # Constructing a binary tree
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    root.right.right = TreeNode(7)

    print(largestBSTSubtree(root))  # Output: 3 (the subtree rooted at node 5 is the largest BST)
# classic tree + DFS (post-order traversal) problem. The key idea is to check for every node whether the subtree rooted at that node is a BST, and if so, compute its size.
# The function `dfs` returns a tuple containing:
# 1. A boolean indicating whether the subtree is a BST.
# 2. The size of the subtree if it is a BST.
# 3. The minimum value in the subtree.
# 4. The maximum value in the subtree.
# The main function `largestBSTSubtree` initializes the maximum size to 0 and calls the `dfs` function on the root of the tree. 
# The `dfs` function performs a post-order traversal, checking each node's left and right subtrees to determine if they are BSTs and calculating their sizes.
# If a valid BST is found, it updates the maximum size accordingly. 
# Complexity
# Time: O(n) — each node visited once
# Space: O(h) — recursion stack (h = height of tree)