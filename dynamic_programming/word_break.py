def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i): # j-> 0 to i-1
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[len(s)]

if __name__ == "__main__":
    print(word_break("leetcode", ["leet", "code"])) # Output: True
    print(word_break("applepenapple", ["apple", "pen"])) # Output: True
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])) # Output: False