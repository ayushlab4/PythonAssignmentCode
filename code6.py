# Ayush Agarwal-20030480008
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a value for n: "))
primes_list = []
i = 2
while len(primes_list) < n:
    if is_prime(i):
        primes_list.append(i)
    i += 1
print("List of first", n, "prime numbers:")
print(primes_list)
print("Ayush_Agarwal_20030480008")