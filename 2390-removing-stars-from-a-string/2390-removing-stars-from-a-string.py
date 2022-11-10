class Solution:
    def removeStars(self, s: str) -> str:
        # Create a stack 
        stack = []
        # Loop through characters of s
        for i in s:
            # If The currecnt character if alphabet append it to stack
            if i.isalpha():
                stack.append(i)
            # If it is a star pop the last element of the stack
            if i == '*':
                stack.pop()

        return ''.join(stack)