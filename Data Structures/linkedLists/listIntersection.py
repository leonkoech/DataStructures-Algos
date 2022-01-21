
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         1->2->3->8->9
# #            5->7->8->9
#         if not headA.next and not headB.next:
#             return headA
#         mySet=set()
#         cur1,cur2=headA,headB
#         while cur1:
# #             break
#             mySet.add(cur1)
#             cur1=cur1.next
#         while cur2:
#             if cur2 in mySet:
#                 return cur2
#             cur2=cur2.next
            
#         return
#         two pointer technique  
        p1,p2=headA,headB
        while True:
            if p1==p2:
                return p1
            if p1.next == p2.next:
                return p1.next
            
            p1=p1.next if p1.next else headB
            p2=p2.next if p2.next else headA
        return p1.val
            