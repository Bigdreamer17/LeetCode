class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        l = 0
        for r in range(len(prices)) :
            if r-1 >= 0 and prices[r] == prices[r-1] - 1 :
                ans += (r-l+1)
            else :
                ans += 1
                l = r
        return ans
       
    
    """
        l = 0 
        ans = len(prices)
        k = 0
        for r in range(1, len(prices)):
            if prices[l] - prices[r] == 1:
                k += 1
            
            l += 1
        leng = k + 1
        # print(leng)
        return ans + leng """