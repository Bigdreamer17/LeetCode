class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for j in s:
            if stack and stack[-1] == j:
                stack.pop()
            else:
                stack.append(j)
        return ''.join(stack)