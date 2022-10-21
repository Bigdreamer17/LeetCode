class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
            return all(any(l <= i <= r for l, r in ranges) for i in range(left, right + 1))
            """
            here is an article that shows how to Check if value exists in a Two-dimensional list in Python 
            https://bobbyhadz.com/blog/python-check-if-element-in-2d-list
        
            """