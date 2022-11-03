class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l = len(arr)
        five_per = int(l * 0.05)
        return mean(arr[five_per:-five_per])