class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = equal = 0
        for i in nums:
            if i < target:
                less += 1
            elif i == target:
                equal += 1
        return list(range(less, less + equal))
        