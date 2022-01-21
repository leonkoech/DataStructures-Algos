#         self.right = right
class Solution:
    def rec(self,root,result):
        if root is not None:
            self.rec(root.left,result)
            result.append(root.val)
            self.rec(root.right,result)
            
            
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         recursive solution
        # result=[]
        # self.rec(root,result)
        # return result
#         stack solution
        
        # myarr.append(current.val)
        # current = root
        # stack=[]
        # myarr=[]
        # while True:
        #     if current is not None:
        #         stack.append(current)
        #         current=current.left
        #     elif stack:
        #         current=stack.pop()
        #         myarr.append(current.val)
        #         current = current.right
        #     else:
        #         break
        # return myarr
        
#         trying to implement queue




        if root is None:
            return
        
        queue=deque([root])
        ans=[]
        current = root
        queue.append(root)
        
        while len(queue)>0:
            if current is not None:
                queue.append(current)
                current = current.left
                
            elif queue:
                node=queue.popleft()
                ans.append(node.val)
                current = node.right
                
            else:
                break
        
        
        return ans
        