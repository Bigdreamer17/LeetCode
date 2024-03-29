# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = None
        curr = head 
        
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            
            if prev is None:
                head = temp
            else:
                prev.next = temp
            
            prev = curr
            curr = curr.next
        return head