class Solution:
    def helper(self,root,arr):
        if root is not None:
            
            self.helper(root.left,arr)
            self.helper(root.right,arr)
            arr.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         recursive solution
         myarr=[]
         self.helper(root,myarr)
         return myarr