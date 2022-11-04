class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(l.pop())
            else:
                ans.append(c)
        return "".join(ans)