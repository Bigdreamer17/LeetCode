class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        s = []
        lenn = -1
        for w in range(len(strs)):
            for j in range(len(strs)):
                if w != j:
                    l = 0 
                    r = 0
                    for r in range(len(strs[j])):
                        if l < len(strs[w]) and strs[j][r] == strs[w][l]:
                            l += 1
                    if l >= len(strs[w]):
                        break
                if j == len(strs) - 1:
                    lenn = max(lenn, len(strs[w]))
        return lenn