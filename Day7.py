word_file = input("Enter a sentence:")

#Write into file
with open("output.txt", 'w') as file:
    file.write(word_file)

#Read from file
with open("output.txt", 'r') as file:
    content = file.read()

words = content.split()
characters = len(content)

print(f"Total number of words:{len(words)}")
print(f"Total number of characters:{characters}")