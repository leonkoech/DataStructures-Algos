# this is a function to join two linked lists
# Given the head of a singly linked list, return true if it is a palindrome.

# this is not in place 
def joinUs(self,list1,list2):
    # list1  = 1->2->3->4->5->7
    # list2  = 5->6->7->8->9->10

    def insert(prev,curr,next):
        # for a singly list
        prev.next = curr
        curr.next = next


    if list1.head is None or list2.head is None:
        return list1 if list1.head is not None else list2 if list2.head is not None else None
    
    current1=list1.head
    current2 = list2.head

    while True:
        if current1.next is None or current2.next is None:
            break

        
        if current1.data < current2.data:
            current1 = current1.next
        elif current1.data == current2.data:
            insert(current1,current2,current1.next)
            current2=current2.next
        else:
            insert(current1.prev,current2,current1)
            current1=current1.next
            current2 = current2.next
    return current1


