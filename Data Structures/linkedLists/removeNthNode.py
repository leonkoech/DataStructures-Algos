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
            return
        
        s,f=head,head
        for _ in range(n):
            f=f.next
        while f:
            if f.next is None:
                s.next=s.next.next
            f=f.next
            s=s.next
        return head
       