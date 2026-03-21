
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    i, j = m, n
    lcs = []
    dp = [[0]*(n+1) for _ in range(m+1)] # create a dp table of size (m+1) x (n+1) initialized with 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]: # if equal add 1 to diagonal value 
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # if not equal take max of left and top value
                
    # Backtrack to find the longest common subsequence string
    while i >0 and j>0:
        if text1[i-1] == text2[j-1]:
            # current character is part of LCS
            lcs.append(text1[i-1])
            i -=1
            j -=1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -=1 # move up
        else:        
            j -=1 # move left

    lcs.reverse()        
    return dp[m][n], "".join(lcs)

if __name__ == "__main__":
    print(longestCommonSubsequence("abcde", "ace")) # Output: 3, "ace"
    print(longestCommonSubsequence("abc", "abc"))   # Output: 3, "abc"
    print(longestCommonSubsequence("abc", "def"))   # Output: 0, ""