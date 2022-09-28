class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        count = 0
        for i in range(len(nums)):
            nums[i] += nums[i -1] if i != 0 else 0
            
            count += d[nums[i] -k]
            d[nums[i]] += 1
        return count
        
        
        
        
        """
        presum = [nums[0]]
        result = 0
        for i in range(len(nums)):
            presum.append(presum[i] + nums[i])
        print(len(presum))
        di = dict(int)
        
        print(di)
        return result 
           """     
        
        