# Create a tuple 
my_tuple = (1, 2, 3, 4, 5) 
  
# Accessing tuple elements 
print(my_tuple[0])  # Output: 1 
print(my_tuple[2])  # Output: 3 
  
# Trying to modify a tuple (this will result in a TypeError) 
my_tuple[0] = 10 
  
# Unpacking tuples 
point = (3, 4) 
x, y = point 
print(x)  # Output: 3 
print(y)  # Output: 4 
  
# Using tuples as keys in dictionaries 
my_dict = {(1, 2): 'hello', (3, 4): 'world'} 
print(my_dict[(1, 2)])  # Output: 'hello' 
print(my_dict[(3, 4)])  # Output: 'world' 
 
In this example, a tuple called my tuple with 5 elements is created.
We then attempt to edit the first element of the tuple, which fails due to the immutability of tuples, then access individual elements of the tuple using indexing.  
  
We also show how to use the x, y = point syntax to break up tuples into independent variables. Finally, we demonstrate how to use tuples, which each represent a point in 2D space and have strings for values, as keys in dictionaries. 
 
