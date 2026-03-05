from typing import List
def partition(s:str) -> List[List[str]]:
    res, sol =[], []
    n = len(s)
    def isPalindrome(x)->bool:
        return x == x[::-1]
    
    def backtrack(i):
        if i ==n:
            res.append(sol[:])
            return
        for j in range(i, n):
            part = s[i:j+1]
            
            if isPalindrome(part):
                sol.append(part)

                backtrack(j+1)
                sol.pop()
    backtrack(0)
    return res

# Time O(n^3) for checking palindrome and generating all possible partitions, every palindrome check takes O(n) and there are O(n^2) possible partitions
# Optimization: we can use dynamic programming to store the results of palindrome checks in a 2D boolean array,
# so that we can check if a substring is a palindrome in O(1) time after an initial O(n^2) preprocessing step.
from typing import List

def partition(s: str) -> List[List[str]]:
    n = len(s)
    res, sol = [], []

    # DP table: dp[i][j] = True if s[i:j+1] is palindrome
    dp = [[False] * n for _ in range(n)]

    # Fill DP table
    for end in range(n):
        for start in range(end + 1):
            if s[start] == s[end] and (end - start <= 2 or dp[start+1][end-1]):
                dp[start][end] = True

    def backtrack(i):
        if i == n:
            res.append(sol[:])
            return

        for j in range(i, n):
            if dp[i][j]:
                sol.append(s[i:j+1])
                backtrack(j + 1)
                sol.pop()

    backtrack(0)
    return res

#Time Complexity: O(n^2) for filling the DP table and O(2^n) for generating all possible partitions in the worst case (when all characters are the same).
#DP build: O(n²)
#Backtracking: O(2^n)


if __name__ == "__main__":
    print(partition("racecar"))            