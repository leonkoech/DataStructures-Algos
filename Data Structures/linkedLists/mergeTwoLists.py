# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
    
        head = ListNode(0,None)
        p=head
        while True:
            if list1 is None:
                p.next = list2
                break
            if list2 is None:
                p.next = list1
                break
            if list1.val < list2.val:
                p.next=list1
                list1=list1.next
            else:
                p.next=list2
                list2=list2.next
            p=p.next
        return head.next
            
        
        
        
        
        
#         current1=list1.head
#         current2 = list2.head
#         listn=ListNode()
#         listn.val=0
#         while True:
#             if current1.next is None or current2.next is None:
#                 break
#             elif current1.val<= current2.val:
#                 listn.next = current1
#                 current1.next
#             else:
#                 listn.next