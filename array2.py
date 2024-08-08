number = (int(input("number")))
a = 0
b = 1
i = 1
# print(a)
# print(b)
while i <= number:
    c = a + b
    print(c)
    a = b 
    b = c 
    i += 1
