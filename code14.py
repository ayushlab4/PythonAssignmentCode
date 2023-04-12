# Ayush Agarwal-20030480008
def count_frequency(numbers):
    frequency_dict = {}
    for num in numbers:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    return frequency_dict

numbers = input("Enter a tuple of integers, separated by commas: ")
numbers = tuple(map(int, numbers.split(",")))
frequency_dict = count_frequency(numbers)
print("Frequency dictionary:", frequency_dict)
print("Ayush Agarwal 20030480008")