# Ayush Agarwal-20030480008
my_list = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    my_list.append(ele)
new_list = []
while my_list:
    min = my_list[0]
    for x in my_list:
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)

print(new_list)