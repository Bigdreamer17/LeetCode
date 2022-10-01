class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        ans = 0
        for i in range(n-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                indx = stack.pop()
                ans = max(ans, i - indx)
        return ans
    """   
        stack = []
        res = 0
        for i in range(len(nums))[::-1]:
            if not stack or nums[i] > stack[-1][0]:
                stack.append([nums[i], i])
            else:
                j = stack[bisect.bisect(stack, [nums[i], i])][1]
                res = max(res, j - i)
        return res
    """
      