# reversing a linked list. This is a basic problem that is asked in interviewws.
# I'll start with singlt linked list then double linked list

# 2->3->5->8->9
#  <- <- <- <-
# driver code to switch the pointers

# singly linked list solution
def switch(current,prev):
    current.next=prev

def singlyLinkedListSolution(self,listo):
    if listo.head is None:
        return listo
    
    current=listo.head

    while current:
        if current.next is None:
            # this would mean that you have reached the end of the linked list
            current=listo.head
        switch(current,current.prev if current.prev is not None else None)
        current=current.next

# doubly linked list solution
def switch2(current,prev,next):
    current.next=prev
    current.prev=next

def doublyLinkedListSolution(self,listo):
    if listo.head is None:
        return listo
    
    current = listo.head

    while current:
        if current.next is None:
            # this would mean that you are at the end of the list
            current = listo.head
        switch2(current,current.prev if current.prev is not None else None,current.next if current.next is not None else None)
        current= current.next