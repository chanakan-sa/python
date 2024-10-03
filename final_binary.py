class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(32)
node45 = TreeNode(45)
node56 = TreeNode(56)
node23 = TreeNode(23)
node78 = TreeNode(78)
node12 = TreeNode(12)
node89 = TreeNode(89)
node34 = TreeNode(34)
node50 = TreeNode(50)
node67 = TreeNode(67)

root.left = node12
root.right = node78

node12.right = node34

node78.left = node50
node78.right = node89

node34.left = node23
node34.right = node67

node50.left = node45
node50.right = node56

def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left,target)
    elif target > node.data:
        return search(node.right,target)

result = search(root,2)
if result:
    print('Found')
else:
    print('Not Found')