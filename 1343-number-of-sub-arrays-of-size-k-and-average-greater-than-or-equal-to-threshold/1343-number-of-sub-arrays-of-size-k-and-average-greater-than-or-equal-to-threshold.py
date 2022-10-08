class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        summ = sum(arr[:k])       
        ans = 0
        if summ // k >= threshold:
                    ans += 1
        for i in range(k, len(arr)):
            summ += arr[i]
            summ -= arr[i - k]
            
            if summ // k >= threshold:
                    ans += 1
        
        return ans