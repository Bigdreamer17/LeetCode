class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        isFalse = True
        
        for i in range(len(l)):
            new= nums[l[i]:r[i]+1]
            new.sort()
            temp = 100001
            isFalse =True
            
            for j in range(len(new)-1):
                if temp == 100001:
                    temp = new[j] - new[j +1]
                    
                if temp != 10001 and new[j] - new[j+1] != temp:
                    isFalse = False
                    break
                temp = new[j] - new[j+1]
            answer.append(isFalse)
            
        return answer