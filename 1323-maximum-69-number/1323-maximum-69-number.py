class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [x for x in str(num)]
        for i in range(len(nums)):
            if nums[i] == '6':
                nums[i] = '9'
                break
        return int("".join(nums))
            
        