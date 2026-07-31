# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        linkedlistLen = 0
        curr = head
        while curr:
            linkedlistLen += 1
            curr = curr.next

        stepsToPrev = linkedlistLen - n
        curr = dummy
        while stepsToPrev:
            stepsToPrev -= 1
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next

         
        