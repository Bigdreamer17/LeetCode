class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums) - 1
        j = len(nums) - 2
        
        return (nums[i]-1) * (nums[j]-1)