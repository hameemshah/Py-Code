import random as r
# i = 0
# while True:
#     i += 1
#     num = r.randint(1, 1000)
#     num2 = r.randint(1, 1000)
#     num3 = r.randint(1, 1000)
#     if num == num2 == num3:
#         break
# print(i)

my_list = []
while len(my_list) != 10000:
    num = int(r.random()*10000)
    if num not in my_list:
        my_list.append(num)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while key < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort(arr):
    for i in range(len(data) - 1):
        swapped = False
        for j in range(len(data)-i-1):
            if(data[j+1] < data[j]):
                data[j+1], data[j] = data[j], data[j+1]
                swapped = True
        if not swapped:
            break
    return data