# Ayush Agarwal-20030480008
def sum_of_even_and_odd_numbers(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    print("Sum of even numbers:", even_sum)
    print("Sum of odd numbers:", odd_sum)
    print("Ayush Agarwal 20030480008")
numbers = input("Enter a list of numbers, separated by spaces: ")
numbers = numbers.split()
numbers = [int(num) for num in numbers]

sum_of_even_and_odd_numbers(numbers)
