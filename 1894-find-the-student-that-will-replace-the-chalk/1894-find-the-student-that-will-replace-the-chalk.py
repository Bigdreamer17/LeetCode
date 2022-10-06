class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        su = sum(chalk)
        maxx = k % su
        cur = chalk[0]
        i = 0 
        while (i <len(chalk)):
            if maxx - chalk[i] >= 0:
                maxx -= chalk[i]
            else:
                return i
            i += 1
       
        return i
            
        