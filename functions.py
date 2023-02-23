# Define a function that takes two numbers as arguments and returns their sum
def add_numbers(a, b):
    return a + b

# Define a function that takes a string as an argument and prints it to the console
def print_message(message):
    print(message)

# Define a function that takes a list of numbers as an argument and returns the largest number
def find_largest_number(numbers):
    largest_number = numbers[0]
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number

# Define a function that takes a dictionary of names and ages as an argument and prints a message for each person
def print_person_details(person_details):
    for name, age in person_details.items():
        print(f"{name} is {age} years old.")

# Call the add_numbers function and print the result
result = add_numbers(2, 3)
print_message(f"The sum of 2 and 3 is {result}.")

# Call the find_largest_number function with a list of numbers and print the result
numbers = [3, 5, 2, 8, 1]
largest_number = find_largest_number(numbers)
print_message(f"The largest number in the list {numbers} is {largest_number}.")

# Call the print_person_details function with a dictionary of person details
person_details = {"Alice": 25, "Bob": 30, "Charlie": 35}
print_person_details(person_details)
