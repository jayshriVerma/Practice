from typing import List

def permutations(nums: List[int]) -> List[List[int]]:
    res, sol = [], []
    used = [False] * len(nums)

    def backtrack():
        if len(sol) == len(nums):
            res.append(sol[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            sol.append(nums[i])
            used[i] = True

            backtrack()

            sol.pop()
            used[i] = False

    backtrack()
    return res

if __name__ == "__main__":
    print(permutations([1, 2, 3])) # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]