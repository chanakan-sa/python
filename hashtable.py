# 1.Starting with an array.
#         0    1    2    3    4    5    6    7    8    9   10
data = [None,None,None,None,None,None,None,None,None,None,None]

# 2.Storing names using a hash function.
def hash_function (value) :
    sum_of_char = 0
    for char in value:
        print(ord(char))
        sum_of_char += ord(char)

    print(sum_of_char)
    # การแปลงเลขให้อยู่ในช่วง 0-9
    index = sum_of_char % 10
    print(index)
    # เพิ่มข้อมูลลง Hash Table (Array)
    data[index] = value
    

hash_function('banana')
hash_function('apple')
hash_function('kiwi')
hash_function('pear')
print(data)
