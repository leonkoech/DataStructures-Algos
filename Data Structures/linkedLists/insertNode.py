# This is the solution to insert nodes either at the beginning or at a particular position from the end or at  the end
# all code will  be listed

# for the instances of this solution the node will be called 'new_node' and it has all the date it needs
# new_node.next=None
# new_node.prev=None
# new_node.data=5

# solutions are also categorized for singly and doubly linked lists with driver codes

# adding at the beginning O(1)
# 2->3->4->5->6
class Node():
    def __init__(self,val) -> None:
        self.data=val
        self.next = None
        self.prev=None
class Solution():
    def addAtBeginning(self,linked):
        if linked.head is None:
            return linked

        head=linked.head
        # for the sake of the example the node is 5 val
        new_node=Node()
        new_node.data=5

        # for a singy linked list
        new_node.next=head
        linked.head = new_node

        # for a doubly linked list
        new_node.next=head
        head.prev=new_node
        linked.head=new_node

# this is a test, idk if it will work
    def atAPosition(self,linked,position):
        if linked.head is None:
            return linked

        
        inner = 0
        current=linked.head

        while current:
            
            # this find the total number of nodes in the linked list
            
            if current.next:
                current=current.next
            else:
                
                # this is after you get to the end of the linked list
                # solution should run at least n+k times giving the solution O(n)
                if inner == position:
                    return current.data
                current=current.prev
                # inner loop count
                inner += 1
        # find the position from the beginning

    # this solution should probablt add a node at the end of the linked list
    def addAtTheEnd(self,linked):
        
        if linked.head is None:
            return linked
        

        new_node=Node()
        new_node.data=5

        current=linked.head
        while current:
            if current.next is None:
                # end
                new_node.prev = current
                # for doubly linked list
                new_node.next = None
                current.next=new_node
                linked.head=new_node
                
            current=current.next


