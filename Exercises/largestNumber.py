# Find the largest number in a List

def find_max(my_list):
    largest = my_list[0]
    for i in my_list:
        if i > largest:
            largest = i
    return largest

