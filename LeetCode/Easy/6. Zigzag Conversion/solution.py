class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        rows = []
        for i in range(numRows):
            rows.append("")

        row = 0
        step = 1

        for c in s:
            rows[row] += c

            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step

        ans = ""
        for word in rows:
            ans += word

        return ans