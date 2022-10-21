class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre = [nums[0]]
        
        for i in range(1, len(nums)):
            pre.append(pre[i-1] + nums[i])
        mini = min(pre)
        n = 1
        while mini + n < 1 :
            n += 1
        return n