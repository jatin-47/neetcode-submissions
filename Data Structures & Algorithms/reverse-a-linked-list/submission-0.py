# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        nxt = head.next
        head.next = None
        while nxt != None:
            # head - current node
            # head.next - next node
            temp = nxt.next
            nxt.next = head
            head = nxt
            nxt = temp
        return head
