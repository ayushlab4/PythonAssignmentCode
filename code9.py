# Ayush Agarwal-20030480008
string = input("Enter a string: ")
char_counts = {}
for char in string:

    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

for char, count in char_counts.items():
    print(f"The character '{char}' occurs {count} time(s) in the string.")
