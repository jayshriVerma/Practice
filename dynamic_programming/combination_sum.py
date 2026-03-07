from typing import List
   
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res, sol = [], []
    n = len(candidates)

    def backtrack(i, target):
        if target == 0:
            res.append(sol[:])
            return
        if i == n or target < 0:
            return

        # Include the current candidate
        sol.append(candidates[i])
        backtrack(i, target - candidates[i])  # Not incrementing i allows for unlimited use of the same candidate
        sol.pop()

        # Exclude the current candidate and move to the next one
        backtrack(i + 1, target)

    backtrack(0, target)
    return res

if __name__ == "__main__":
    print(combinationSum([2, 3, 6, 7], 7)) # Output: [[2, 2, 3], [7]]