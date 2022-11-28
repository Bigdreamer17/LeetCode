# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = []
        node = head
        while node:
            ans.append(node.val)
            node = node.next
        return int(''.join(str(i) for i in ans), 2)