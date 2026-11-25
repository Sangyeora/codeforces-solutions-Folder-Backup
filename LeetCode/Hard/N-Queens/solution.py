class Solution:
    def solveNQueens(self, n):
        ans = []
        cols = []

        def place(row):
            if row == n:
                board = []

                for col in cols:
                    line = "." * col + "Q" + "." * (n - col - 1)
                    board.append(line)

                ans.append(board)
                return

            for col in range(n):
                ok = True

                for i in range(row):
                    if cols[i] == col:
                        ok = False
                        break

                    if abs(cols[i] - col) == row - i:
                        ok = False
                        break

                if ok:
                    cols.append(col)
                    place(row + 1)
                    cols.pop()

        place(0)
        return ans