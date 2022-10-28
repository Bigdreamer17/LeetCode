class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        nums.sort()
        l = 0 
        r = 1
        while r < len(nums):
            if nums[l] % 2 != 0 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            else:
                r += 1 """
        return sorted(nums, key = lambda x : x % 2)
   # return sorted(nums, key = lambda x : x % 2)