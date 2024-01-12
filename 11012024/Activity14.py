
my_list = [1, 7, 4, 3, 2, 9, 15, 6]

largest_number = my_list[0]


for num in my_list:
    if num > largest_number:
        largest_number = num

    print("The largest number of the list :", largest_number)