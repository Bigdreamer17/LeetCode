class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = r = 0
        
        while r < len(s) and l < len(g):
            if s[r] >= g[l]:
                l += 1
            r += 1
        return l
    
    """
        print(g)
        print(s)
        if sum(g) < sum(s):
            return len(g)
        elif len(g) == len(s):
            l = r = 0
            while r < len(s):
                if g[l] >= s[r]:
                    c += 1
                l += 1
                r += 1
        elif len(g) < len(s):
            r = 0
            for l in range(len(g)):
                if s[r] >= g[l]:
                    c += 1
                r += 1
        else:
            l = 0
            for r in range(len(s)):
                if s[r] >= g[l]:
                    c += 1
                l += 1

       # return c """