# การแก้ไขปัญหาการชน
# 1.ประกาศอาร์เรย์
data_set = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

# 2.สร้าง Hash function
def hash_function (value):
    sum_of_char = 0
    for char in value :
        sum_of_char += ord(char)

    return sum_of_char % 10

# 3.สร้าง Function การเพิ่มข้อมูล
def add_function (value):
    index = hash_function(value)
    data = data_set[index]

    if value not in data :
        data.append(value)

# 4. ทดสอบเพิ่มข้อมูล
add_function('banana')
add_function('apple')
add_function('kiwi')
add_function('mango')

print(data_set)

# 5.สร้าง function การค้นหา
def search_function(value):
    index = hash_function(value)
    data = data_set[index]

    if value in data :
        print('Found')
    else :
        print('Not Found')

# 6.ค้นหาข้อมูล
search_function('mango')
