import random

# Starting with an array.
data = [None, None, None, None, None, None, None, None, None, None, None]

# ฟังก์ชันแฮชที่มีการสุ่ม
def hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)

    print(sum_of_char)
    
    # ใช้ส่วนที่สุ่มเพื่อปรับการคำนวณดัชนี
    random_factor = random.randint(0, 9)
    index = (sum_of_char + random_factor) % 10
    
     # เพิ่มข้อมูลลงใน Hash Table (Array)
    data[index] = value

hash_function('earn')
hash_function('apple')
hash_function('kiwi')
hash_function('pear')
hash_function('puck')

print(data)
