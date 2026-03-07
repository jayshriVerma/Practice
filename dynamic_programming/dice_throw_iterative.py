def no_of_ways(n, m, x):
    # Create a table to store results of subproblems
    dp = [[0]*(x+1) for _ in range(n + 1)]

    # Base case: There is one way to get sum 0 with 0 dice
    dp[0][0] = 1

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, x + 1):
            for k in range(1, min(m, j) + 1): #don't need to check all faces if target sum j is less than m
                dp[i][j] += dp[i - 1][j - k] # add ways from previous row (i-1 dice)for sum j-k

    return dp[n][x]


if __name__ == "__main__":
    n = 3  # number of dice
    m = 6  # number of faces on each die
    x = 12  # target sum
    print(no_of_ways(n, m, x))  # Output: 25


# Space complexity of the iterative DP approach is O(n*x) due to the dp table storing results for each combination of n and x.
# The time complexity is O(n*x*m) because we fill the dp table by iterating through n, x, and m.  
# 
# visualization of the dp table for n=3, m=6, x=12: dp[3][12] = 25
# Dice\Sum |0 1 2 3 4 5 6 7 8 9 10 11 12
# --------------------------------------
# 0 dice   |1 0 0 0 0 0 0 0 0 0 0  0  0
# 1 dice   |0 1 1 1 1 1 1 0 0 0  0  0  0
# 2 dice   |0 0 1 2 3 4 5 6 5 4  3  2  1
# 3 dice   |0 0 0 1 3 6 10 15 21 25 27 27 25

# dp[i][j] = ways to get sum j using i dice  
# Space Optimized Version: O(space complexity O(x) instead of O(n*x))
def dice_ways(m, n, x):
    dp = [0]*(x+1)
    dp[0] = 1

    for _ in range(n):
        new = [0]*(x+1)
        for s in range(x+1):
            if dp[s] > 0:
                for face in range(1, m+1):
                    if s+face <= x:
                        new[s+face] += dp[s]
        dp = new

    return dp[x]

# The space optimized version uses a single array to store the number of ways to achieve each sum with the current number of dice, 
# and updates it iteratively for each die. This reduces the space complexity to O(x) while maintaining the same time complexity of O(n*x*m).

#VARIANT: number of ways to get a sum ≤ X when all dice are thrown. return sum(dp[n][0...X]) or sum(dp[n]) since dp[n][j] = 0 for j > x.
# We don't need to check all m faces if j is small.
def countWays(m, n, x):
    dp = [[0]*(x+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(1, x+1):
            for k in range(1, min(m, j)+1):
                dp[i][j] += dp[i-1][j-k]

    return sum(dp[n])
# Number of Dice Rolls With Target Sum
# Return ways to get exact sum X, but answer must be mod 10⁹ + 7.
# the number can become huge n=30, m=30 target = 500 the count can exceed python integer limits so result % (10^9 + 7) or dp[i][j] %= MOD , 


