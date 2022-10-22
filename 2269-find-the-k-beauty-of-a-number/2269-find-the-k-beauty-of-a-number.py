class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        for i in range(len(str(num)) - k + 1):
            n = str(num)
            div = (int(n[i:i+k]))
            if div and num % div == 0:
                ans += 1
        return ans