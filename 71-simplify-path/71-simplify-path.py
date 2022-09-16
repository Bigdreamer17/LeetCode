class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        
        for i in range(len(path)):
            if path[i] == "..":
                if stack:
                    stack.pop()
            elif path[i] != "" and path[i] != ".":
                stack.append('/' + path[i])
        
        return ''.join(stack) if stack else '/'
        
            