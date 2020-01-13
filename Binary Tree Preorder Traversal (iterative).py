def preorderTraversal(self, root: TreeNode) -> 'List[int]':
        result = []
        stack = []
        
        while root or stack:
                #append the parent node value and go to the left node 
                if root:
                        result.append(root.val)
                        #store root value in stack for future traversal
                        stack.append(root)
                        root = root.left
                
                #when there is no left node, go to the right node
                else:
                        root = stack.pop().right
        return result
