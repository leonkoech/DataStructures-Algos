# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def myfun(self,cur,n):
    #         if cur.next is None:
    #             return 1
    #         mynumber=self.myfun(cur.next,n)+1
    #         if mynumber==n+1:
    #                 cur.next= cur.next.next
    #         return mynumber
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next is None:
            return None
            
        dummy=ListNode(0,head)
        pointer1, pointer2 = dummy,dummy
        for i in range(n):
            pointer2=pointer2.next
        while pointer2.next:
            
               pointer2=pointer2.next
               pointer1= pointer1.next
        
        pointer1.next=pointer1.next.next
                
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         recursive solution
#         checks if current item has a next
#         if current does not have a next
#         return one
#         get the number of current item adding one to the recursive function from the end
#         if the current item number is equal to n+1 meaning it's the prev node, delete the next node
        
        
#         if head.next is None:
#             return
#         num = self.myfun(head,n)
#         if n+1>num:
#                     nextnode = head.next
#                     head.val=nextnode.val
#                     head.next=None if head.next.next is None else nextnode.next
        
#         return head
#         1->2->3->4->5-6
#         p1 p2
          # two pointer technique
        
#             move the fast pointer n number of steps ahead of slow
#             when fast reaches the end delete the slow pointer
#             1->2->3->4->5
#             1
#             1->2->3->4->5
#                   p1       p2


        
        
            
            
# 
#         dummy=ListNode(0,head)
        
#         slow,fast=dummy,dummy
#         for _ in range(n):
#                 fast=fast.next
                
#         while fast.next:
#                 fast=fast.next
#                 slow=slow.next
#         slow.next=slow.next.next
#         return dummy.next
                    