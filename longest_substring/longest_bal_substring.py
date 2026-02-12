# Longest balanced substring with repeated characters
# A substring of s is called balanced if all distinct characters in the substring appear the same number of times
    
def longestsubstring(s: str)-> int:
    n= len(s)
    ans= 0
    

    for i in range(0, n):
        freq = [0] * 26
        distinct =0
        max_freq=0
        for j in range(i, n):
            idx = ord(s[j])-ord('a')

            if freq[idx] == 0:
                distinct +=1  
            freq[idx] += 1
            max_freq = max(max_freq, freq[idx])
            length = j-i + 1

            if length == distinct * max_freq:
                ans = max(ans, length)

    return ans        

# Time:O(n² × 26)

if __name__ == "__main__":
    print(longestsubstring("abbad")) # o/p 4 a,b appears twice
    print(longestsubstring("zabbc")) # o/p 3 a,b appears twice and c appears once
    print(longestsubstring("abcde")) # o/p 1 all characters appear once