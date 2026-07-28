# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow = head
        fast = head.next
        #find middle and split list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        #reverse second half of the list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #merge the 2 lists
        second = prev
        first = head
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        


        



        