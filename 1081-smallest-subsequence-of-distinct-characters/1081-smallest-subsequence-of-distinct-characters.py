class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # A dictionary to hold our chars last position 
        l = {}
        for i in range(len(s)):
            l[s[i]] = i
        # create a stack to track our ans and a set to check which once we will be looking for
        stack = []
        v  = set()
        
        for i in range(len(s)):
            #Loop through s and if s[i] is not in stack add it to both stack and set 
            if s[i] not in stack:
                #if it is and stack is not empty and the last item of stack is > s[i] and the value of stack[-1] in our dict is > i pop from both stack and set 
                while(stack and stack[-1] > s[i] and l[stack[-1]] > i):
                    v.remove(stack.pop())
                
                stack.append(s[i])
                v.add(s[i])
        
        return ''.join(stack)