# Longest Substring Where Every Character Appears At Least K Times (Harder)

def longestsubstring_with_k(s: str, k: int) -> int: 
    n = len(s)
    ans = 0
    
    for i in range(n):
        freq = [0] * 26
        count_less_than_k = 0
        
        for j in range(i, n):
            idx = ord(s[j]) - ord('a')
            
            freq[idx] += 1
            
            # When character appears first time
            if freq[idx] == 1:
                count_less_than_k += 1
            
            # When it reaches k → now valid
            if freq[idx] == k:
                count_less_than_k -= 1
            
            if count_less_than_k == 0:
                ans = max(ans, j - i + 1)
    
    return ans

# every character appears at least k times
# Time: O(n² × 26)
if __name__ == "__main__":
    print(longestsubstring_with_k("aaabb", 3)) # Output: 3 
    print(longestsubstring_with_k("ababbc", 2)) # Output: 4
    print(longestsubstring_with_k("aaabbbccd", 2)) # Output: 8