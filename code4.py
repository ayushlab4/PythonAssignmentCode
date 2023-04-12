# Ayush Agarwal-20030480008
# prompt user to enter list of integers
num_list = input("Enter a list of integers separated by space: ")
# convert input string to list of integers
num_list = list(map(int, num_list.split()))
# calculate sum of integers in list
sum_num = sum(num_list)
# display result
print("The sum of all integers in the list is:", sum_num)
