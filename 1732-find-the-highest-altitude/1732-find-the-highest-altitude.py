class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum  = [0]
        
        for i in gain:
            prefix_sum.append(i + prefix_sum[-1])
        ans = max(prefix_sum)
        if ans <= 0:
            return 0
        else:
            return ans 