days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 

print(days_of_week[0]) 

my_list = [5, 3, 1, 4, 2] 

print(len(my_list)) # Output: 5 

my_list.append(6) 
print(my_list) # Output: [5, 3, 1, 4, 2, 6] 

my_list.insert(0, 0) 
print(my_list) # Output: [0, 5, 3, 1, 4, 2, 6] 

my_list.remove(3) 
print(my_list) # Output: [0, 5, 1, 4, 2, 6] 

my_list.sort() 
print(my_list) # Output: [0, 1, 2, 4, 5, 6]
