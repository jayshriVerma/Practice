from typing import List

def combinations(nums: List[int]) -> List[List[int]]:
    res, sol = [], []
    n = len(nums)

    def backtrack(start):
        res.append(sol[:])

        for i in range(start, n):
            sol.append(nums[i])

            backtrack(i + 1)

            sol.pop()

    backtrack(0)
    return res

if __name__ == "__main__":
    print(combinations([1, 2, 3])) # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
