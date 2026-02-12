# Longest Substring With Equal 0s and 1s

def longest_balanced_substring(s):
    n = len(s)
    max_len = 0
    count = 0
    for i in range(n):
        if s[i] == '1':
            count += 1
        else:
            count -= 1
        if count == 0:
            max_len = max(max_len, i + 1)
    return max_len

if __name__ == "__main__":
    print(longest_balanced_substring("1101001100")) # Output: 6    
# Input: "1101001"
# Output: 6
# Explanation: "101001" has 3 zeros and 3 ones.