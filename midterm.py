
# number = int(input("ป้อนตัวเลขจำนวนเต็ม :"))

# if number % 2 == 0 :
#     print("เลขคู่")
# elif number % 2 != 0 :
#     print("เลขคี่")




# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i = i + 1
#     print(sum)





def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

celsius_temp = float(input("ใส่อุณหภูมิองศาเซลเซียส: "))

fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
fahrenheit_temp = celsius_to_fahrenheit(fahrenheit)

print("อุณหภูมิฟาเรนไฮต์: {fahrenheit_temp}")



# array = [5,2,3,10,2,2,9,3,2,7]

# count_2 = array.count(2)
# count_3 = array.count(3)

# print("เลข 2 ซ้ำกันทั้งหมด" ,count_2, "ครั้ง")
# print("เลข 3 ซ้ำกันทั้งหมด" ,count_3, "ครั้ง")