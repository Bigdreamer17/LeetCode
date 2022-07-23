class Solution:
    def hIndex(self, citations: List[int]) -> int: 
        citations.sort(reverse = True)
        ans = 0
        
        if max(citations) >= 1:
            for i in range(len(citations)):
                if ans < citations[i]:
                    ans += 1
                
         
        return ans
    