# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         stack solution
            current = root
            stack=[]
            preorder=[]
            while True:
                if current is not None:
                    stack.append(current)
                    preorder.append(current.val)
                    current=current.left
                elif stack:
                    current=stack.pop()
                    current=current.right
                else:
                    break
            return preorder
                    

        
    