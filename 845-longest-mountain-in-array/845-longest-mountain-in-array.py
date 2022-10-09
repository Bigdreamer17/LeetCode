class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n, max_len = len(arr), 0
        state, length = 0, 1
        for i in range(n-1):
            if state in [0, 1] and arr[i+1] > arr[i]:
                state, length = 1, length + 1
            elif state == 2 and arr[i+1] > arr[i]:
                state, length = 1, 2
            elif state in [1, 2] and arr[i+1] < arr[i]:
                state, length = 2, length + 1
                max_len = max(length, max_len)
            else:
                state, length = 0, 1
                
        return max_len
    """
        coun = 1
        ans = 0
        for i in range(1, len(arr)-2):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                peak = i
                while peak > 0 and arr[peak] > arr[peak-1]:
                    peak -= 1
                    coun += 1
                while peak < len(arr) - 1 and arr[peak] > arr[peak + 1]:
                    peak += 1
                    count += 1
        ans = max(coun, ans)
        return ans """