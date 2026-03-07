from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res, sol = [], []
    used = [False] * len(nums)

    def backtrack():
        if len(sol) == len(nums):
            res.append(sol[:])
            return

        for i in range(len(nums)):

            if used[i]:
                continue

            # skip duplicates
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            sol.append(nums[i])
            used[i] = True

            backtrack()

            sol.pop()
            used[i] = False

    backtrack()
    return res

#Given a list of numbers that may contain duplicates, return all unique permutations.
# Permutation II is a classic backtracking problem where you generate all unique permutations of a list that may contain duplicate numbers.
# It appears on LeetCode as Permutations II.

# Sort the array first
# Use a used[] array to track which elements are included in the current permutation
# Skip duplicates using this condition

if __name__ == "__main__":
    print(permuteUnique([1,1,2])) # Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]  
