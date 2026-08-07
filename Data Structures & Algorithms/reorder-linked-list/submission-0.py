# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseLL(head):
            curr, nxt = None, head
            while nxt:
                temp = nxt.next
                nxt.next = curr
                curr = nxt
                nxt = temp
            return curr

        length = 0
        mov = head
        while mov:
            mov = mov.next
            length += 1
        
        newHead = head
        idx = length//2 -1 if length%2 == 0 else length//2
        while idx and newHead:
            newHead = newHead.next
            idx -= 1
        
        print(newHead.val, head.val)
        newHead.next = reverseLL(newHead.next)
        newHead = newHead.next

        secondHead = newHead
        while head != newHead:
            temp = head.next
            head.next = secondHead
            head = temp

            if head == newHead:
                break
            temp = secondHead.next
            secondHead.next = head
            secondHead = temp
