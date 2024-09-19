# โครงสร้างข้อมูลแบบ Tree

# สร้าง Funtion กำหนดค่า

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# การเก็บข้อมูลลงโครงสร้างแบบ Tree
rootnode = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')
nodeEARN = TreeNode('EARN')

# การกำหนด Eage หรือกิ่ง
rootnode.left = nodeA
rootnode.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

nodeE.left = nodeEARN

# print(rootnode.data) 
# print(nodeF.data)
# print(rootnode.left.data)
# print(rootnode.left.left.data)

# test ครั้งที่1
print(rootnode.data)
print(rootnode.right.data)
print(rootnode.right.left.data)
print(rootnode.right.left.left.data)
