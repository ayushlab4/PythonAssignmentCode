# Ayush Agarwal-20030480008
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def next_prime_number(num):
    num += 1
    while True:
        if is_prime(num):
            return num
        num += 1
num = int(input("Enter a number: "))
next_prime = next_prime_number(num)
print("The next prime number after", num, "is", next_prime)
print("Ayush Agarwal 20030480008")