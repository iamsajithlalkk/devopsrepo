n = int(input("Enter a number:"))
sum = 0

for i in range(1,n+1):
    print(i,end=" ")
    sum += i

print("\nSum =", sum)