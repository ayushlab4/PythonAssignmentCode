# Ayush Agarwal-20030480008
# prompt user to enter value of n
n = int(input("Enter a value for n: "))
# create list of squares of first n natural numbers using for loop
squares_list = []
for i in range(1, n+1):
    squares_list.append(i**2)
# display list of squares
print("List of squares of the first", n, "natural numbers:")
print(squares_list)