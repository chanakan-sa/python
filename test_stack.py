stacks = []

stacks.append('ก็อต')
stacks.append('นิค')
stacks.append('เบียร์')
stacks.append('ที')
stacks.append('ปั๊ก')

print(stacks)

# ลบข้อมูลตำแหน่งบนสุด
stacks.pop(-1)
print(stacks)

# การหาตำแหน่งบนสุด
print(stacks[-1])


size = len(stacks)
print(size)


isEmpty = len(stacks) == 0
print(isEmpty)

print(stacks)

stacks.pop(-1)
print(stacks)
stacks.pop(0)
print(stacks)

