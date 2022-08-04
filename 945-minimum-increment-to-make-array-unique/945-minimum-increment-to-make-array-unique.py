class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        ans = defaultdict(int)
        maxx = nums[0] + 1
        for i in range(len(nums)):
            if nums[i] in ans:
                count += abs(nums[i] - maxx)
                ans[maxx] = 1
                maxx += 1
            else:
                ans[nums[i]] = 1
                maxx  = nums[i] + 1
        return count