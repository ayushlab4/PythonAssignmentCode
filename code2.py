# Ayush Agarwal-20030480008
strings = []
for i in range(5):
    string = input("Enter string " + str(i+1) + ": ")
    strings.append(string)
def ascii_value(string):
    return ord(string[0])
sorted_strings = sorted(strings, key=ascii_value)
print("Sorted strings:")
for string in sorted_strings:
    print(string)