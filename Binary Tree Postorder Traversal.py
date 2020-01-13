# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#Recursive Solution
    def postorderTraversalR(self, root: TreeNode) -> List[int]:
        array=[]
        return self.dummy(root,array)
    def dummy(self, root, array):
        if root is not None:
            self.dummy(root.left, array)
            self.dummy(root.right, array)
            array.append(root.val)
        return array
    

#Iterative Solution
	def peek(self, stack): 
        if len(stack) > 0: 
            return stack[-1] 
        return None
    def postorderTraversalI(self, root: TreeNode) -> List[int]:
        stack=[]
        res = []
        while(True): 
            while (root): 
                if root.right is not None: 
                    stack.append(root.right) 
                stack.append(root) 
                root = root.left 
            root = stack.pop() 
            if (root.right is not None and self.peek(stack) == root.right): 
                stack.pop()   
                stack.append(root) 
                root = root.right 
            else: 
                res.append(root.val)  
                root = None

            if (len(stack) <= 0): 
                break
        return res