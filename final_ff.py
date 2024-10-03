nodedata = ['A','B','C','D','E','F']

matrix  = [
    [0, 1, 1, 0, 0] ,  # Edge for A
    [1, 0, 0, 1, 1] , # Edge for B
    [1, 0, 0, 1, 0] ,  # Edge for C
    [0, 1, 1, 0, 1] ,   # Edge for D
    [0, 1, 0, 1, 0]  # Edge for E
     [0, 1, 0, 1, 0]  # Edge for F
]

def show_matrix(matrix):
    for row in matrix:
        print(row)

# show_matrix(matrix)

def show_connect(matrix,nodedata):
    print("Connection of Node")
    # len = 4 , range กำหนดช่วงเริ่มจาก 0,1,2,3
    for i in range(len(nodedata)):
        print(f"{nodedata[i]}: ",end="")
        for j in range(len(nodedata)):
            if matrix[i][j]:
                print(nodedata[j], end="")
        print()

show_connect(matrix,nodedata)