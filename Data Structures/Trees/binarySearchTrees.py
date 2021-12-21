class Node():
    def __init__(self,data):
        self.left=None,
        self.right=None,
        self.data=data
# Given a BST and a key K. If K is not present in the BST, Insert a new Node with a value equal to K into the BST. 
# Note: If K is already present in the BST, don't modify the BST.
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.right< key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root