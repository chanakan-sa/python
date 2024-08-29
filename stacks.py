# 1. สร้างโครงสร้างข้อมูลแบบ stack
stacks = [];

# 2. Push การเพิ่มข้อมูลลง stack
stacks.append('apple');
stacks.append('orange');
stacks.append('pear');
stacks.append('peach');
stacks.append('cherry');
stacks.append('grape');

print(stacks);

# 3. Pop การลบข้อมูลตำแหน่งบนสุด
stacks.pop();
print(stacks);

# 4. Peek การหาตำแหน่งบนสุด
print(stacks[-1]);

# 5. Size การหาขนาดของ stack
size = len(stacks);
print(size);


# 6. isEmpty ตรวจสอบว่า stacks ว่างหรือไม่
isEmpty = len(stacks) == 0
print(isEmpty)

