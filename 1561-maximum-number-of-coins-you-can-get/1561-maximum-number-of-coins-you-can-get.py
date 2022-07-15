class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = piles[len(piles)//3:]
        a = 0
        i = 0 
        
        while i  < len(piles):
            a += piles[i]
            i += 2
        
        return a