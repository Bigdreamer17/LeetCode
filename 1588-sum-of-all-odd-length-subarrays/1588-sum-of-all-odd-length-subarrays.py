class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        
        for i in range(n):
            even_away = ((i // 2) + 1) * ((n - i - 1) // 2 + 1)
            odd_away = ((i + 1) // 2) * ((n - i) // 2)
            ans += arr[i] * (even_away + odd_away)
        return ans 
    """ Full explantion https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/854298/O(n)-time-O(1)-space-step-by-step-explanation-Python """