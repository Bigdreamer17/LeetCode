class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        
        for i in range(len(path)):
            if path[i] == "" or path[i] == ".":
                pass
            elif path[i] == "..":
                if stack:
                    stack.pop()
            else:
                stack.append('/' + path[i])
        return ''.join(stack) if stack else '/'
        
            