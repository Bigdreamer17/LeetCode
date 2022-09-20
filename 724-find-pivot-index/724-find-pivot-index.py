class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum =[nums[0]]
        rig = [0 for i in range(len(nums))]
        rig[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            presum.append(presum[i - 1] + nums[i])
            
        for i in range(len(nums)-2,-1,-1):
            rig[i] = rig[i + 1] + nums[i]
            
        print(rig, presum)
        for i in range(len(nums)):
            if rig[i] == presum[i]:
                return i
        return -1