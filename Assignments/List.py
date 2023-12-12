def interchange_first_last(my_list):
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    return my_list

def list_size(my_list):
    return len(my_list)

def check_element(my_list, element):
    return element in my_list

