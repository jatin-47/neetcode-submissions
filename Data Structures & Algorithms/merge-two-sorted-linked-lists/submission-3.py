# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list1.val <= list2.val:
            resultHead = list1
            list1 = list1.next 
        else:
            resultHead = list2
            list2 = list2.next

        movingHead = resultHead
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                movingHead.next = list1
                list1 = list1.next 
            else:
                movingHead.next = list2
                list2 = list2.next 
            movingHead = movingHead.next
        movingHead.next = list1 or list2
        return resultHead
        