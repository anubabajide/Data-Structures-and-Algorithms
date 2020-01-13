# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#Recursive Solution
    def inorderTraversalR(self, root: TreeNode) -> List[int]:
        array=[]
        return self.dummy(root,array)
    def dummy(self, root, array):
        if root is not None:
            self.dummy(root.left, array)
            array.append(root.val)
            self.dummy(root.right, array)
        return array
    

#Iterative Solution
	def inorderTraversalI(self, root: TreeNode) -> List[int]:
        stack = []  
        res = [] 
        while True: 
            if root is not None: 
                stack.append(root)           
                root = root.left  
            elif(stack): 
                root = stack.pop() 
                res.append(root.val)  
                root = root.right  
            else: 
                break
        return res