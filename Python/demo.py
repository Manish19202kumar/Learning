#-Reverse List
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)

#-Odd No. in a List-
my_list = [1, 2, 3, 4, 5]
odd_numbers = [num for num in my_list if num % 2 != 0]
print(odd_numbers)

#--Even NO. in a List--
my_list = [1, 2, 3, 4, 5]
index1, index2 = 1, 3  # indices of elements to swap
my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
print(my_list)

#-Swap two element in a List
my_list = [1, 2, 3, 4, 5]
index1, index2 = 1, 3  # indices of elements to swap
my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
print(my_list)

#-Duplicate Values in a List-
my_list = [1, 2, 2, 3, 4, 4, 5]
duplicates = set(x for x in my_list if my_list.count(x) > 1)
print(list(duplicates))