import collections
//Definition of a Node
class Node:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

//Helper Function to mirror a node
def generateMirror(node,copy):
    copy.val=node.val
    if node.right:
        copy.left=Node(node.right.val)
    if node.left:
        copy.right=Node(node.left.val)
    return copy

//Helper Function to print a node using In-Order Traversal
def Print(node):
    stack=[]
    result=[]
    while stack or node:
        if node:
            stack.append(node)
            node=node.left
        else:
            node=stack.pop()
            result.append(node.val)
            node=node.right
    return result

//Main function that visits each Node using Level-Order Traversal
def BFSTraversal(node):
    queue=collections.deque()
    queue1=collections.deque()
    result=Node(node.val)
    queue.append(node)
    queue1.append(result)

    while queue:
        cur=queue.popleft()
        copy=queue1.popleft()
        if cur is None:
            continue 
        copy=generateMirror(cur,copy)
        if (cur.left):
            queue.append(cur.left)
            queue1.append(copy.right)
        if (cur.right):
            queue.append(cur.right)
            queue1.append(copy.left)
    print(BFSprint(node),BFSprint(result))

T=Node(4)
T.left=Node(2)
T.right=Node(6)
T.left.left=Node(1)
T.left.right=Node(3)
T.right.left=Node(5)
T.right.right=Node(7)

print(BFSTraversal(T))
