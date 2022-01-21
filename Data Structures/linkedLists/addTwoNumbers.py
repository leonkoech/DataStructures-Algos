# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         create a dummy node to store values
#        if sum>9 carry one to the next node val
#         carry = 1
#          9+1 to 9+9= x   
#          x-10 carry one
        dummy = ListNode(0,None)
        dummyTail=dummy
        carry=0
        
        while l1 or l2 or carry:
           
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry,s=divmod(v1+v2+carry,10)
            
            dummyTail.next=ListNode(s)
            dummyTail=dummyTail.next
            
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
            