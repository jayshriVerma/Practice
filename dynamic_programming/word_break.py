def word_break(s, word_dict):
    wordSet = set(word_dict)  # Convert list to set for O(1) lookups
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i): # j-> 0 to i-1
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return dp[len(s)]

if __name__ == "__main__":
    print(word_break("leetcode", ["leet", "code"])) # Output: True
    print(word_break("applepenapple", ["apple", "pen"])) # Output: True
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])) # Output: False

  
# Time complexity: O(n²) for aboce code because of the nested loops and substring check
# i loop → n
# j loop → n
# substring check → O(1) average
# Space complexity: O(n) for dp array

def word_break(s, wordDict):
    dp = [False] * (len(s)+1)
    dp[0]=  True
    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i] and s[i: j+1] in wordDict:
                dp[j+1] = True
    return dp[-1]
# Time Complexity: O(n³) because of substring check substring check → n

function wordBreak(s: string, wordDict: string[]): boolean {
    const wordSet = new Set(wordDict);

    const dp: boolean[] = new Array(s.length + 1).fill(false);
    dp[0] = true;

    for(let i =1; i <= s.length; i++) {
        for(let j = 0; j < i; j++) {
            if (dp[j] && wordSet.has(s.substring(j,i))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[s.length];
}