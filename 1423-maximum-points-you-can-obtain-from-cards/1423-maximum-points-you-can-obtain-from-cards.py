class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # the last test case answer is 248
        total = sum(cardPoints)
        rem = len(cardPoints) - k
        sub_sum = sum(cardPoints[:rem])
        summ = sub_sum
        
        for i in range(rem,len(cardPoints)):
            sub_sum += cardPoints[i]
            sub_sum -= cardPoints[i - rem]
            
            summ = min(summ,sub_sum)
        
        
        return total - summ
        
        
        
        
        """ 
       cur_sub = sum(cardPoints[:k])
        res = [cur_sub]
        
        for i in range(1, len(cardPoints)-k+1):
            cur_sub = cur_sub - cardPoints[i-1]
            cur_sub = cur_sub + cardPoints[i+k-1]
            
            res.append(cur_sub)
        
        return max(res)"""