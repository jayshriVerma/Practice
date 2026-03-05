from typing import List


def subset(nums:List[int]) -> List[List[int]]:
    n = len(nums)
    res, sol = [], []
    def backtrack(i):
        if i == n:
            res.append(sol[:])
            return
        # don't pick nums[i], move on and backtrack on next index
        backtrack(i + 1)
        # include the current element
        sol.append(nums[i])
        # backtrack with the current element included
        backtrack(i + 1)
        sol.pop()
      
    backtrack(0) # call this to start the backtracking process(generate the tree) from the first index
    return res
  
if __name__ == "__main__":
    print(subset([1, 2, 3])) # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]] 