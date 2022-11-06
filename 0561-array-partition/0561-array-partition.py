class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sorting nums
        nums.sort()
        n = len(nums)
        # Initializing maximum sum
        max_sum = 0
        # looping through nums and stepping by 2 so first i is nums[0] then its 1 + 2 = nums[3]
        for i in range(0,n,2):
            max_sum += nums[i]
        return max_sum