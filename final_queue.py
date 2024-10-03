queue = []

queue.append('apple')
queue.append('orange')
queue.append('pear')
queue.append('peach')
queue.append('cherry')

print(queue)

print(queue[0])
print(queue[-1])

size = len(queue)
print(size)

queue.pop(0)
queue.pop(0)
print(queue)