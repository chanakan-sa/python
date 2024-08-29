# 1. การสร้างข้อมูลแบบ Queue
queues = []

# 2. Enqueue การเพิ่มข้อมูล
queues.append(2)
queues.append(3)
queues.append(4)
queues.append(5)
queues.append(6)
queues.append(7)
queues.append(8)

print(queues)

# 3. Dequeue การลบข้อมูลตำแหน่ง Front
queues.pop(0)
print(queues)

# หาตำแหน่งแรกและตำแหน่งสุดท้าย
print(queues[0])
print(queues[-1])

# 5. Size การหาขนาดของ Queue
size = len(queues)
print(size)

# 6. isEmpty การตรวจสอบค่าว่าง
isEmpty = len(queues) == 0
print(isEmpty)
