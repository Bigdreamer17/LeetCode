class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(popped)
        i = 0 
        for j in pushed:
            stack.append(j)
            while stack and i<n and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return stack ==[]