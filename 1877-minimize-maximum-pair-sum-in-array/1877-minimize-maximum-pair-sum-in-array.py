class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        j = len(nums) - 1
        new = []
        for i in range(len(nums)//2):
            new.append(nums[i]+nums[j-i])

        return max(new) 	
