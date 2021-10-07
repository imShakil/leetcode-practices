class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        ans = ""
        cnt = len(words)
        for word in words:
            ans += word[::-1]
            if cnt != 1:
                ans += " "
                cnt -= 1
        return ans
