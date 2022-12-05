# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_len = 0
        l =  node = head
        
        while l:
            list_len += 1
            l = l.next
        mid = list_len // 2
        
        
        c = 0
        while node:
            if c == mid:
                return node
            else:
                c += 1
                node = node.next
        return None 