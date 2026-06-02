student_data = {}

for i in range(3):
    name = input(f"Enter student {i+1} name:")
    mark = input(f"Enter mark:")

    student_data[name] = mark

print(student_data)
print(f"Topper: {max(student_data, key = student_data.get)} with {max(student_data.values())}")
# print(max(student_data.values()))
# print(max(student_data, key = student_data.get))