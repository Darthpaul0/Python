# Write a program to remove duplicates in a list.

my_list = [1, 2, 2, 3, 4, 5, 6, 9, 6, 7, 8, 9]
uniques = []

for number in my_list:
    if number not in uniques:
        uniques.append(number)
print(uniques)
