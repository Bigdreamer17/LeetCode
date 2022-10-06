class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = float("inf")
        summ = 0
        while right < len(nums):
            summ += nums[right]
            while summ >= target:
                summ -= nums[left]
                ans = min(ans, right - left + 1)  
                left += 1
            right += 1
        if ans == float("inf"):
            return 0
        
        return ans 