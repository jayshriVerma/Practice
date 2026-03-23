#3402. Minimum Operations to Make Columns Strictly Increasing
from typing import List
def minimumOperations(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    op = 0
    for c in range(n):
        prev = grid[0][c]
        for r in range(1,m):
            if grid[r][c] <= prev:
                needed = prev+1
                op += needed - grid[r][c]
                prev = needed
            else:
                prev = grid[r][c]
    return op 
    
if __name__ == "__main__":
    print(minimumOperations([[1,2,3],[4,5,6],[7,8,9]])) # Output: 0
    print(minimumOperations([[3,2],[1,3],[3,4],[0,1]]))
    print(minimumOperations([[0,0],[0,0]])) # Output: 2