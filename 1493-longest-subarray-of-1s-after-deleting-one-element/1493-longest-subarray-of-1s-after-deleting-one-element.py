class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        curr = 0
        best = 0
        arr_leng = len(nums) 
        while r < arr_leng:
            if nums[r] == 0:
                curr += 1
            while curr > 1:
                if nums[l] == 0:
                    curr -= 1
                l += 1
            r += 1
            best = max(best, r - l - 1)
        return best
        