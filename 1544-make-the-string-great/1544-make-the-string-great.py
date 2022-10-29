class Solution:
    def makeGood(self, s: str) -> str:
        # From the Solution page
        while len(s) > 1:
            find = False
            
            for i in range(len(s) - 1):
                curr , nex = s[i], s[i + 1]
                
                if abs(ord(curr) - ord(nex)) == 32:
                    s = s[:i] + s[i + 2:]
                    find = True
                    break
                    
            if not find:
                break
        return s