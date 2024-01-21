#Author: Hameem Hussain Shah

# Interchange first and last element in a list
def interchange_first_last(my_list):
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    return my_list

# Swap two elements of a list
def swap(my_list, first, second):
    if first not in my_list or second not in my_list:
        return "One or more elements not present in the list"
    
    index_first = my_list.index(first)
    index_second = my_list.index(second)

    my_list[index_first], my_list[index_second] = my_list[index_second], my_list[index_first]
    
    return my_list

# Find length of a list
def list_size(my_list):
    return len(my_list)

# Check if element exists in list
def check_element(my_list, element):
    return element in my_list

#Different ways to clear list
def clr(my_list):
    my_list.clear()

def clr2(my_list):
    for _ in range(len(my_list)):
        my_list.pop()

# Reversing a list
def rev(my_list):
    my_list.reverse()

# Find sum of elements in list
def sum_list(my_list):
    return sum(my_list)

# Multliply all numbers in list
def mul_list(my_list):
    product = 1
    for num in my_list:
        product *= num
    return product

# Smallest in list
def small(my_list):
    return min(my_list)

# Largest in list
def large(my_list):
    return max(my_list)

# Second largest element in list
def second_largest(my_list):
    my_list.remove(max(my_list))
    return max(my_list)

