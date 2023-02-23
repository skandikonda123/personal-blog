# Define a function that returns the sum of two numbers
def add_numbers(a, b):
    return a + b

# Define a function that returns a list of even numbers from a given list
def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Define a function that returns a dictionary of person details
def get_person_details(name, age):
    return {"name": name, "age": age}

# Define a function that returns another function
def get_greeting_function():
    def greeting_function(name):
        return f"Hello, {name}!"
    return greeting_function

# Call the add_numbers function and print the result
result = add_numbers(2, 3)
print(f"The sum of 2 and 3 is {result}.")

# Call the get_even_numbers function with a list of numbers and print the result
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(f"The even numbers in the list {numbers} are {even_numbers}.")

# Call the get_person_details function and print the result
person_details = get_person_details("Alice", 25)
print(f"Person details: {person_details}.")

# Call the get_greeting_function function and use the returned function to print a greeting
greeting_function = get_greeting_function()
greeting = greeting_function("Bob")
print(greeting)
