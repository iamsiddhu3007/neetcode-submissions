# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # num1 = ""
        # num2 = ""
        # while l1:
        #     num1 = str(l1.val) + num1
        #     l1 = l1.next
        # while l2:
        #     num2 = str(l2.val) + num2
        #     l2 = l2.next

        # res = str(int(num1) + int(num2))

        # dummy = ListNode(None)
        # curr = dummy
        # for char in reversed(res):
        #     curr.next = ListNode(int(char))
        #     curr = curr.next

        # return dummy.next
        dummy = ListNode(None)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:        
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            currSum = val1+val2+carry
            if currSum >= 10:
                carry = 1
                currSum -= 10
            else:
                carry = 0
            curr.next = ListNode(currSum)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next




            