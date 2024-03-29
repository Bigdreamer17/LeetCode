class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                k -= 1
                stack.pop()
            stack.append(i)
            
        stack = stack[:len(stack) - k]
        ans = "".join(stack)
        return str(int(ans)) if ans else "0"
        