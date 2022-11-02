class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        l = r = 0
        while l < len(target):
            if target[l] != arr[r]:
                return False
            l += 1
            r += 1
        return True 