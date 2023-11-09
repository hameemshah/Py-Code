def merge_sort(list):
    """Sort a list in ascending order
        uses divid and conquer strategie
        
        Take O(n log n) time
        """
    
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """Divide the unsorted list at midpoint at sublist
        Return two sublists left and right
        
        Takes O(log n) time
        """
    midpoint = len(list) // 2
    return list[:midpoint],list[midpoint:]

def merge(left, right):
    """Merges two lists sorting them in process
        and returning the new list
        
        Runs in O(n) time
        """
    
    l = []
    j = 0
    i = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
        
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])

my_list = [4, 6, 19, 23, 25, 29, 43, 66, 82, 89, 99]
print(verify_sorted(my_list))
