from typing import List
def findAnagrams(s: str, p: str) -> List[int]:
    if len(s) < len(p):
        return []
    need = [0] *26
    for c in p:
        need[ord(c)-97] +=1
    need_count = sum(1 for x in need if x > 0)

    window = [0]*26
    left = valid =0
    res = []
    for right, c in enumerate(s):
        idx = ord(c)-97
        window[idx] +=1

        if window[idx] == need[idx]:
            valid +=1

        if right- left +1 >len(p):
            l_idx = ord(s[left]) -97
            if window[l_idx] == need[l_idx]:
                valid -=1
            window[l_idx] -=1
            left +=1
        if right - left +1 == len(p) and valid == need_count :
            res.append(left)
    return res           
    # fixed length sliding window + frequency arary + match counter
    # Time complexity O(n), space :O(1), where n is the length of s
    # need[26] counts p , window[26] counts current window
    # valid variable tracks matched character types,avoiding arary comparison
    # Expand right, shrink left, update window and valid
    # When window size equals p length and valid == needCount, found anagram
    #438. find all anagrams in a string
    # Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
    # An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

if __name__ == "__main__":
    print(findAnagrams("cbaebabacd", "abc")) # Output: [0, 6]
    print(findAnagrams("abab", "ab"))        # Output: [0, 1, 2]    