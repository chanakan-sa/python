class NN:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prve = None

node1 = NN(3)
node2 = NN(5)
node3 = NN(10)
node4 = NN(15)


node1.next = node2
node2.prve = node1
node2.next = node3
node3.prve = node2
node3.next = node4
node4.prve = node3

currentnode = node1
while currentnode:
    print(currentnode.data)
    currentnode = currentnode.next

currentnode = node4
while currentnode:
    print(currentnode.data)
    currentnode = currentnode.prve


# print(node1)
# print(node1.data)


# print(node2)
# print(node2.data)
# print(node1.next)


# print(node3)
# print(node3.data)
# print(node2.next)


# print(node4)
# print(node4.data)
# print(node3.next)


