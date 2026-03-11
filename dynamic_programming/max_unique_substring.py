
def maxUniqueSplit(s: str) -> int:
    n = len(s)
    def backtrack(i,seen):
        if i == n:
            return 0
        max_splits = 0
        for end in range(i+1, n+1):
            substring = s[i:end]
            if substring not in seen:
                seen.add(substring)
                max_splits = max(max_splits, 1+backtrack(end, seen))
                seen.remove(substring)
        return max_splits            

    return backtrack(0, set())
    
# Time: O(n *2^n) for each character either include in the current substring or start a new substring, that doubles possible outcomes
# Space: O(n) bcoz we maintain a set of seen substrings and the recursion stack can go as deep as n in the worst case. 
if __name__ == "__main__":
    print(maxUniqueSplit("ababccc")) # Output: 5

# Input: s = "ababccc"
# Output: 5
# Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
# Example 2:

# Input: s = "aba"
# Output: 2
# Explanation: One way to split maximally is ['a', 'ba']. Splitting like ['a', 'b', 'a'] is not valid as you have 'a' multiple times.    