# การทำงานของ linkedlists
# ต้องการเก็บข้อมูล 3,5,10,15

# การสร้างคลาส Node สำหรับการกำหนดค่า
class NN:
    def __init__(self, data):
        self.data = data
        # self.data = 3
        self.next = None
        # self.next = null
        self.prve = None

# ประกาศตัวแปร
node1 = NN(3)
node2 = NN(5)
node3 = NN(10)
node4 = NN(15)
# node1 = NN(3)
# print(node1)  # address ในหน่วยความจำตัวมันเอง
# print(node1.data)  # ข้อมูลที่เก็บในnode1
# print(node1.next)  # ตำแหน่งข้อมูลตัวถัดไป

node1.next = node2
node2.next = node3
node3.next = node4

# การเข้าถึงข้อมูลทุกตัว
currentnode = node1

# node1 = address, node1.data = 3, node1.next = ตำแหน่งตัวถัดไป
while currentnode:
    print(currentnode.data)
    currentnode = currentnode.next