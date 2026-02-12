# Longest Substring With Equal Frequency of K Characters


def longestsubstring(s: str, k: int) -> int:
    """Given a string s, return the length of the longest substring where:
    There are exactly K distinct characters
    Each character appears the same number of times"""
    n = len(s) 
    ans = 0 
    for i in range(n): 
        freq = [0] * 26 
        distinct = 0 
        max_freq = 0 
        for j in range(i, n): 
            idx = ord(s[j]) - ord('a') 
            if freq[idx] == 0: 
                distinct += 1 
            freq[idx] += 1 
            max_freq = max(max_freq, freq[idx]) 
            length = j - i + 1 
            if distinct == k and length == distinct * max_freq: 
                ans = max(ans, length) 
    return ans

# Time Complexity: O(n^2 * 26) where n is the length of the string. 
# The outer loop runs n times, and the inner loop also runs n times. 
# The frequency array has a constant size of 26 for lowercase letters, so it contributes a constant factor to the time complexity.
# Input: s = "aaabbbccc", k = 3
# Output: 9
# Explanation: The longest substring with equal frequency of 3 characters is "aaabbbccc" where 'a', 'b', and 'c' each appear 3 times.
if __name__ == "__main__":
    print(longestsubstring("aaabbbccc", 3)) # Output: 9