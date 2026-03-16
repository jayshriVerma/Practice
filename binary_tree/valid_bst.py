def is_validBST(root)->bool:
    def inorder_traversal(node, result):
        if node is None:
            return True
        if not inorder_traversal(node.left): 
            return False
        nonlocal prev
        if prev >= node.data: 
            return False
        prev = node.data
        return inorder_traversal(node.right)
    prev = float('-inf')
    return inorder_traversal(root)

# Time Complexity: O(n) where n is the number of nodes in the tree, since we visit each node once.
# Space Complexity: O(h) where h is the height of the tree, due to the recursive call stack. In the worst case (skewed tree), this can be O(n). In a balanced tree, it would be O(log n).
# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.    
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees. 
# here comparing the current node's value with the previous node's value in the in-order traversal allows us to ensure that the values are strictly increasing, which is a requirement for a valid BST.