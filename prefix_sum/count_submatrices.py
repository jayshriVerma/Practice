def countsubmatrices(grid:list[list[int]], k :int) -> int:
    m, n = len(grid), len(grid[0])
    ans = 0
    pref =[[0] *(n+1)  for _ in range(m+1)]
    # pref matrix is used to store the cumulative sum of the grid values. This allows us to quickly calculate the sum of any submatrix in constant time.
    # pref = [[0] * (n + 1) for _ in range(m + 1)] creates a 2D list (matrix) of size (m+1) x (n+1) filled with zeros. This matrix will be used to store the prefix sums of the original grid. The extra row and column (m+1 and n+1) are added to handle edge cases when calculating submatrix sums without needing additional checks for out-of-bounds errors.
    ans = 0
    for r in range(m):
        for c in range(n):
           # The 2D Prefic sum formula is used to calculate the sum of a submatrix defined by its top-left corner (r1, c1) and bottom-right corner (r2, c2) in constant time. The formula is:
            pref[r+1][c+1] = (grid[r][c] + pref[r][c+1] +pref[r+1][c]- pref[r][c])

            if pref[r+1][c+1] <=k:
                ans +=1
            else:
                break
    return ans            

           
if __name__ == "__main__":
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    k = 2
    print(countsubmatrices(grid, k))