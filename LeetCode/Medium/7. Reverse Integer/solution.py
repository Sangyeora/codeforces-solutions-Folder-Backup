class Solution:
    def reverse(self, x):
        s = str(x)
        negative = False

        if x < 0:
            negative = True
            s = s[1:]

        s = s[::-1]

        limit = "2147483647"
        if negative:
            limit = "2147483648"

        if len(s) == 10 and s > limit:
            return 0

        if negative:
            s = "-" + s

        return int(s)