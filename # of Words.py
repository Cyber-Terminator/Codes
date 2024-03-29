essay = input("Enter your essay here: ")
words = 1

for letter in essay:
    if letter in " ":
        words += 1

print("There are " + str(words) + " words in that essay")
