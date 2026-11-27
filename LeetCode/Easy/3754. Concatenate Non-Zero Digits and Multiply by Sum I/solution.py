class Solution:
    def sumAndMultiply(self, n):
        x = 0
        total = 0

        for c in str(n):
            if c != "0":
                digit = int(c)
                x = x * 10 + digit
                total += digit

        return x * total