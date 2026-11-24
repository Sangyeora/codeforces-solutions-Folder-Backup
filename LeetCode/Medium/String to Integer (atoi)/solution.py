class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        ans = 0

        while i < n and s[i] == " ":
            i += 1
        if i < n:
            if s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "+":
                i += 1

        while i < n and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")
            ans = ans * 10 + digit
            i += 1

        ans = ans * sign

        if ans > 2147483647:
            return 2147483647
        if ans < -2147483648:
            return -2147483648

        return ans