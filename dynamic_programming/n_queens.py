
def solveNQueens(n: int):
    res = []
    board = [["."] * n for _ in range(n)]

    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue

            board[r][c] = "Q"
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return res


if __name__ == "__main__":
    print(solveNQueens(4)) # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    print(solveNQueens(1)) # Output: [["Q"]]
    
    