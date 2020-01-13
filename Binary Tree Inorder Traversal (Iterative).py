def inorderTraversal(self, root: TreeNode) -> List[int]:
	#Create stack to store the un-traversed nodes
	stack = []  
	#to store the results
	res = [] 

	#infinite loop
	while True: 

		#find the left-most value in the tree
		if root is not None: 
			#add the untraveresed root to the stack to keep the data for later traversal 
			stack.append(root)
			#update root to left side, 
			root = root.left
			
		# activates when left-most item is gotten
		elif(stack): 
			#left-most item is retrieved and appended
			root = stack.pop() 
			res.append(root.val)  
			#right-value is checked since that left-most item could be a parent [left-parent-right]
			root = root.right  
			
		#breaks the loop when stack is empty and tree is at the end
		else: 
			break
	return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
