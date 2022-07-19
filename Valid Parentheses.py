class Solution:
    def isValid(self, s: str) -> bool:
        
        close = {"(" : ")", "[" : "]", "{" : "}"} 
        opens = []
        
        for p in s:
            if p in close.keys():
                opens.append(p)
            elif opens == [] or p != close[opens.pop()]:
                False
        
        return opens == []
        
        replace = True
        while replace:
            start_length = len(s)
            for inner in ["{}", "()", "[]"]:
                s = s.replace(inner, "")
            if start_length == len(s):
                replace = False
        
        return s == ""
            
            
        