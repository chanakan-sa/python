data_set = [[],[],[],[],[],[],[],[],[],[]]

def hash_function (value):
    sum_of_char = 0
    for char in value :
        sum_of_char += ord(char)

    return sum_of_char % 10

def add_function (value):
    index = hash_function(value)
    data = data_set[index]

    if value not in data :
        data.append(value)

add_function('banana')
add_function('apple')
add_function('kiwi')
add_function('mango')
add_function('cherry')
add_function('orange')
add_function('peach')

print(data_set)

def search_function(value):
    index = hash_function(value)
    data = data_set[index]

    if value in data :
        print('Found')
    else :
        print('Not Found')

search_function('mango')