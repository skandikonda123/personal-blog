numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum += number

print("The sum of the even numbers is:", even_sum)

This code defines a list of numbers called numbers, and sets an initial value of 0 for the variable even_sum.
It then uses a for loop to iterate over each element in the numbers list. For each number, it checks if the number is even by using the modulo operator % to see if it is divisible by 2. 
If the number is even, it adds it to the even_sum variable. Finally, it prints out the total sum of the even numbers in the list.
