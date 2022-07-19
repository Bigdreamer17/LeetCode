class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for i, j in count.items():
            freq[j].append(i)
        
        ans = []
        for k in range(len(freq) - 1, 0, -1):
            for i in freq[k]:
                ans.append(i)
                if len(ans) == k:
                    return ans