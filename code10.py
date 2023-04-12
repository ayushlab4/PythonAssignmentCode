# Ayush Agarwal-20030480008
def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

def lcm(a, b):
    lcm = (a * b) // gcd(a, b)
    return lcm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("LCM of", a, "and", b, "is", lcm(a, b))