from array import array

def sum_of_array(my_array):
    return sum(my_array)

def largest_in_array(my_array):
    return max(my_array)

def rotate(my_array, num=1, dir='l'):
    if num >= len(my_array):
        return "Please enter value less than length of array"
    my_array2 = my_array[num:len(my_array)]
    my_array2.extend(my_array[:num])
    return my_array2

def split(my_array, split):
    start , end = 0 , len(my_array) - 1
    for start in range(split):
        my_array[start] , my_array[end] = my_array[end], my_array[start]
    return my_array

def monotonic(my_array):
    if len(my_array) == 1:
        return my_array[0]
    if not my_array[0] < monotonic(my_array[1:]):
        return False
    return True

