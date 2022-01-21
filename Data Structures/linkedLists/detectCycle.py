class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#         find duplicates using hashmap
#         hashmap={}
#         cur=head
#         if cur is None:
#             return 
#         while cur.next:
#             if cur in hashmap:
#                 return True
#             else:
#                 hashmap[cur] = cur
#                 cur=cur.next
#         return False
#         set approach
            # myset=set()
            # if head is None:
            #     return
            # while head.next:
            #     if head in myset:
            #         return True
            #     myset.add(head)
            #     head=head.next
            # return False
#             slow and fast pointers
            slow,fast=head,head
            if head is None:
                return
            
            while fast and fast.next:
                    
                    fast=fast.next.next
                    slow=slow.next
                    if fast == slow:
                        return True
                    
            return False
    
    