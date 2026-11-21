class Solution:
    def lengthOfLongestSubstring(self, s):
        word = ""
        ans = 0

        for c in s:
            while c in word:
                word = word[1:]

            word = word + c
            ans = max(ans, len(word))

        return ans