class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = {}
        for i in range(len(strs)):
            strr = "".join(sorted(strs[i]))
            c[strr] = [strs[i]] + c.get(strr, [])
         
        return c.values()