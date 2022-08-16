# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0 
        start = node = head
        
        while start:
            length += 1
            start = start.next
        
        middle = length // 2
        
        
        counter = 0 
        while node:
            if counter == middle:
                return node
            else:
                counter += 1
                node = node.next
        return None