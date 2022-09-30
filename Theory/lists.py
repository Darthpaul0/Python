# Find the largest number in a List

my_list = [1, 20, 5, 60, 7, 8, 9]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i
print(largest)
