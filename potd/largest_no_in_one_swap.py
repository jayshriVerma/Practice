def largestStringAfterSwap(s: str) -> str:
    s = list(s)
    
    # Store last occurrence of each character
    last = {c: i for i, c in enumerate(s)}
    
    for i in range(len(s)):
        # Check characters larger than current
        for d in sorted(last.keys(), reverse=True):
            if d > s[i] and last[d] > i:
                j = last[d]
                s[i], s[j] = s[j], s[i]
                return "".join(s)
    
    return "".join(s)

# Time Complexity

# O(n · k log k) (k = number of unique characters)
# First return → used when a swap happens.It is inside the loop because we return immediately after the single allowed swap.
# Last return → used when no swap is needed (string already largest)
# i/p:"768"  o/p:"867"
# Key Idea:
# For each character, know the last occurrence of every digit/character.
# Traverse the string from left to right.
# For each position, check if there exists a larger character later in the string.
# If yes, swap with the rightmost occurrence of the largest possible character and stop (only one swap allowed).