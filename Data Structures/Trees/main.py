

def solution(A):
    # base case
    if max(A)<=0:
            return 1
    else:
        start=1
        for b in range(start,len(A)+start+1):     
           
            if b not in A:
                return b
            elif b==len(A)+1:
                return b
class linkedList():
    def __init__(self,head=None):
        self.head=head
class node():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def createList(one,two,three):
    list1=linkedList()
    node1=node(one,two)
    node2=node(two,three)
    node3=node(three,None)
    list1.head(node1)
    node1.next=node2
    node2.next=node3
def SolutionB():
    #a [1->,2,5]
    #b [1,3,4]
    listA=createList(1,2,5)
    listB=createList(1,3,4)
    # check for the head in listA
    current = listA.head
    currentb=listB.head
    sentinel=node(20)
    # [20,1,1,2,3]
    # [20->prev1->prev2-]
    prev=sentinel

    while current and currentb:
        if current.val <= currentb.val:
            prev.next = current
            current =current.next
        else:
            prev.next = currentb
            currentb = currentb.next
        #
        prev=prev.next
        # current=current.next

    print (listA.head)
                
SolutionB()
