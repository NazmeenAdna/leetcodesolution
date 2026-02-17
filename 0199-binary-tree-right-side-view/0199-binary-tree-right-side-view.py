# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        level=0
        self.rightView(root,level,res)
        return res
    def rightView(self,root,level,res):
        if root is None:
            return 
        if level == len(res):
            res.append(root.val)
        self.rightView(root.right,level+1,res)
        self.rightView(root.left,level+1,res)