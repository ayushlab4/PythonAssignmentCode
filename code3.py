# Ayush Agarwal-20030480008
# prompt user to enter list of integers
num_list = input("Enter a list of integers separated by space: ")
# convert input string to list of integers
num_list = list(map(int, num_list.split()))
# find greatest number in list
max_num = max(num_list)
# display result
print("The greatest number in the list is:", max_num)