import input

data = input.my_list

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