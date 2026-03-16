'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
        def dfs(self, node, k, current_sum, prefix):
            if node is None:
                return 0
            
            current_sum += node.data
            
            count = prefix.get(current_sum - k, 0)
            
            prefix[current_sum] = prefix.get(current_sum, 0) + 1
            
            count += self.dfs(node.left, k, current_sum, prefix)
            count += self.dfs(node.right, k, current_sum, prefix)
            
            prefix[current_sum] -= 1
            
            return count
        def countAllPaths(self, root, k):
            prefix = {0: 1}
            return self.dfs(root, k, 0, prefix)

if __name__ == "__main__":
    # Example usage:
    # Constructing a binary tree
    root = [8, 4, 5, 3, 2, None, 2, 3, -2, None, 1]
    k = 7
    #Output: 3
    Node = Node(0)  # Create an instance of Node to call the method
    print(Node.count_all_paths_with_sum_k(root =[8, 4, 5, 3, 2, None, 2, 3, -2, None, 1], k=7))

# - As you traverse the tree (DFS), maintain the running sum from root to current node.
# - Use a HashMap to store how many times each prefix sum has occurred.
# - At each node, check if (runningSum - k) exists in the map. If yes, that means there’s a path ending at this node with sum = k.
# - Recurse into children, updating the map.
# - Backtrack (remove current node’s contribution before returning).

# - Time Complexity: O(n) (each node visited once).
# - Space Complexity: O(n) for HashMap.