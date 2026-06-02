num = input("Enter a number:")
print(type(num))
try:
    num = float(num)
    if num > 0:
        print("The number is Positive")
    elif num < 0 :
        print("The number is Negative.")
    else:
        print("The number is Zero.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
print(type(num))