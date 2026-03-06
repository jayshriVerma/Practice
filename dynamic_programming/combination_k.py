def k_combination(n, k):
    res, sol = [], []

    def backtrack(start):
        if len(sol) == k:
            res.append(sol[:])
            return

        for i in range(start, n + 1):
            sol.append(i)

            backtrack(i + 1)

            sol.pop()

    backtrack(1)
    return res

if __name__ == "__main__":
    print(k_combination(5, 3)) # Output: [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]
    print(k_combination(4, 2)) # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]