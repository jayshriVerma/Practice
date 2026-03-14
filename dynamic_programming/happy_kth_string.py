# 1415. The k-th Lexicographical String of All Happy Strings of Length n
def getHappyString(n: int, k: int) -> str:
    res, sol = [], []
    chars = ['a', 'b', 'c']

    def backtrack(start):
        if len(sol) == n:
            res.append(''.join(sol))
            return

        for c in chars:
            if not sol or sol[-1] != c:
                sol.append(c)

                backtrack(start + 1)

                sol.pop()

    backtrack(0)
    return res[k - 1] if k <= len(res) else ""

if __name__ == "__main__":
    print(getHappyString(1, 3)) # o/p "c"
    print(getHappyString(1, 4)) # o/p ""
    print(getHappyString(3, 9)) # o/p "cab"
    
# The above backtracking solution generates all happy strings and then retrieves the k-th one.
# However, we can directly compute the k-th happy string without generating all of them, which is more efficient.    

def getHappyString(n: int, k: int) -> str:
    total = 3 * (2 ** (n - 1))
    if k > total:
        return ""
    
    res = []
    chars = ['a', 'b', 'c']
    block = 2 ** (n - 1)
    first_char_index = (k - 1) // block
    res.append(chars[first_char_index])
    k -= first_char_index * block
    for i in range(n-1):
        block //= 2
        prev = res[-1]

        options = [c for c in chars if c != prev]
        index = (k - 1) // block

        res.append(options[index])
        k -= index * block
    return ''.join(res)

if __name__ == "__main__":
    print(getHappyString(1, 3)) # o/p "c"
    print(getHappyString(1, 4)) # o/p ""
    print(getHappyString(3, 9)) # o/p "cab"    
    

# Input: n = 3, k = 9
# Output: "cab"
# Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
# the above code calculates the total number of happy strings of length n, checks if k is within that range, and then constructs the k-th happy string by determining the appropriate characters 
# at each position based on the remaining options and the block size.Much faster than generating all 3 * 2^(n-1) strings.notice the pattern of blocks in lexicographical order and derive the greedy math solution.
# Time:  O(n)
# Space: O(n)
# This pattern appears in many problems like k-th permutation / k-th lexicographical string / k-th combination.
# The core idea is skip whole blocks instead of generating everything.
# At each position:
# index = (k-1) // block_size
# choose element[index]
# remove it from available choices
# k = k % block_size
