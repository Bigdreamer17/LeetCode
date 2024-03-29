class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i in num:
            while stack and k and stack[-1] > i:
                stack.pop()
                k -= 1
                
            if stack or i is not '0':
                stack.append(i)
        if k:
            stack = stack[0:-k]
        return ''.join(stack) or '0'