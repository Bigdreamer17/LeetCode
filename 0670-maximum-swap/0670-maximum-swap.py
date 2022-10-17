class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        max_ = len(num) - 1
        l = r = 0
        
        for i in range(len(num)- 1, -1, -1):
            if num[i] > num[max_]:
                max_ = i
            elif num[i] < num[max_]:
                l = i
                r = max_
        num[l], num[r] = num[r], num[l]
        return int(''.join([str(x) for x in num]))