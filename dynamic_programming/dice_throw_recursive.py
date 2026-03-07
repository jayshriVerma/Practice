def no_of_ways_recursive(n, m, x, memo=None):
    if memo is None:
        memo = {}
    
    # Base case: There is one way to get sum 0 with 0 dice
    if n == 0 and x == 0:
        return 1
    if n == 0 or x <= 0:
        return 0
    
    # Check if the result is already computed
    if (n, x) in memo:
        return memo[(n, x)]
    
    total_ways = 0
    for k in range(1, min(m, x) + 1):
        total_ways += no_of_ways_recursive(n - 1, m, x - k, memo)
    
    # Store the computed result in the memoization table
    memo[(n, x)] = total_ways
    return total_ways

# solve this problem using recursion with memoization to optimize the overlapping subproblems.
# The recursive approach would involve trying all possible outcomes for each die and summing the results, 
# while storing previously computed results in a memoization table to avoid redundant calculations.    
# Time complexity of the recursive approach with memoization is O(n*x*m) in the worst case, where n is the number of dice, x is the target sum, and m is the number of faces on each die. 
# The space complexity is O(n*x) due to the memoization table storing results for each combination of n and x.   