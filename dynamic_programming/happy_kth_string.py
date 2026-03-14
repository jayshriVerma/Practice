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
