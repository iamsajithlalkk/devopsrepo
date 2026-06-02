def check_prime(n):
    print(n)
    if n <= 1: 
        return False
    print(n**0.5)
    for i in range(2, int(n**0.5)+1):
        print(i)
        print(type(i))
        if n % i == 0:
            return False
    return True

num = int(input("Enetr a number:"))

if check_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")