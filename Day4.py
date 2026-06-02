numbers  = []

for i in range(5):
    num = float(input(f"Enter the {i+1} number:"))
    numbers.append(num)

print("List", numbers)
print("Max", max(numbers))
print("Min:", min(numbers))
print("Average:", sum(numbers) / len(numbers))