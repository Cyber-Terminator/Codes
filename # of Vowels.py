word = input("Enter a word: ")

vowel_count = 0

vowels = "aeiouAEIOU"

for letter in word:
    if letter in vowels:
        vowel_count += 1

print("There are " + str(vowel_count) + " vowels in your word.")
