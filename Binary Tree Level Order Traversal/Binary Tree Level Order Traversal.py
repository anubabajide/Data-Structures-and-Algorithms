def levelOrder(self, root: TreeNode) -> List[List[int]]:
	if not root: return []
	queue=[root]
	res=[]
	final=[]
	while queue:
	    for _ in range (len(queue)):
		root=queue.pop(0)
		res.append(root.val)
		if root.left:
		    queue.append(root.left)
		if root.right:
		    queue.append(root.right)
	    final.append(res)
	    res=[]
	return final
	
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
