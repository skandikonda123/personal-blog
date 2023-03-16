# create a 2D list
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print all elements of the list using nested loops
for row in my_list:
    for element in row:
        print(element)

# modify each element of the list using nested loops
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        my_list[i][j] = my_list[i][j] * 2

# print the modified list
print(my_list)
