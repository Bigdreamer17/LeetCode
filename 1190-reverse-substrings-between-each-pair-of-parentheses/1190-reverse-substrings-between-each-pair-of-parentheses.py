class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = ""
        li = []
        for i in range(len(s)):
            if s[i] == '(':
                li.append(i)
            elif s[i] == ')':
                temp = s[li[-1] : i + 1]
                s = s[:li[-1]] + temp[::-1] + s[i + 1:]
                del li[-1]
        for i in range(len(s)):
            if (s[i] != ')' and s[i] != '('):
                ans += (s[i])
        return ans
    