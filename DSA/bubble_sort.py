from data import my_list1

def bubble_sort(arr):
    for i in range(len(my_list1) - 1):
        swapped = False
        for j in range(len(my_list1)-i-1):
            if(my_list1[j+1] < my_list1[j]):
                my_list1[j+1], my_list1[j] = my_list1[j], my_list1[j+1]
                swapped = True
        if not swapped:
            break
    return my_list1