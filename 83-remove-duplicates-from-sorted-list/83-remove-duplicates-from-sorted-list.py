# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head

        while first and first.next:
            if first.next.val == first.val:
                first.next = first.next.next
            else:
                first = first.next

        return head