# การทำ Binary Search Tree

# สร้าง Class สำหรับการกำหนดค่าข้อมูล
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# กำหนดโครงสร้างข้อมูลแบบ Binary Search Tree
root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

# การกำหนด Edge หรือกิ่ง
root.left = node7
root.right = node15
# test ครั้งที่2
# node right จะมีค่ามากที่สุด
# node parent จะมีค่ามากกว่าซ้ายแต่น้อยกว่าขวา
# node left จะมีค่าน้อยที่สุด
node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node18

node18.right = node19

# สร้าง Funtion  สำหรับการค้นหา
def search(node, target):
    # ถ้าค่าที่ส่งเข้ามาเป็นค่าว่างให้ส่งกลับ
    if node is None:
        return None
    # ถ้าสิ่งที่รับเข้ามามีค่าเท่ากับ Root Node
    elif node.data == target:
        return node
    # ถ้าสิ่งที่รับเข้ามามีค่าน้อยกว่า
    elif target < node.data:
        return search(node.left,target)
    # ถ้าสิ่งที่รับเข้ามามีค่ามากกว่า
    elif target > node.data:
        return search(node.right,target)

# การค้นหาหรือ Search
result = search(root,2)
if result:
    print('Found')
else:
    print('Not Found')


