class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r = [nums[0]]
        
        
        for i in range(1,len(nums)):
            r.append(r[i-1] + nums[i])
        
        return r