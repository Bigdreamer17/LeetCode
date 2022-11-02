class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        l = r = 0
        count = 0
        
        while l < len(heights) and r < len(expected):
            if heights[l] != expected[r]:
                count += 1
            l += 1
            r += 1
        return count