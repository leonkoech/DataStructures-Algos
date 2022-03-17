# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorder(self,root,arr):
    #         if root is None:
    #             return 
    #         self.inorder(root.left,arr)
    #         arr.append(root.val)
    #         self.inorder(root.right,arr)
        
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         '''
#         make sure theres root
#         means for every node.left in 1 a node.left should exist in 2
#         and the node.left should be equal 
#         arr=[]
#         def inorder(self,root,arr)
#             if root is None:
#                 return 
#             self.inorder(root.left,arr)
#             arr.append(root.val)
#             self.inorder(root.left,arr)
        
        
#         arr1=self.inorder(p)
#         arr2=self.inorder(q)
        
#         if arr1 != arr2:
#             return False
#         return True
        
        
#         if p is None or n is None:
#                 return 
        
#         if self.inorder(p.left,arr) != self.inorder(q.left,arr) or self.inorder(p.right,arr) != self.inorder(q.right,arr):
#         return False
#         else: 
#             return True
#         '''
# '''

# write a recursive function that will return boolean
# use and or gates 


# if not p and not q:
#      return True
# if not p or not q:
#         return False
# if p.val==q.val:
#         return False
# return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

# '''

                if not p and not q:
                     return True
                if not p or not q:
                        return False
                if p.val!=q.val:
                        return False
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)