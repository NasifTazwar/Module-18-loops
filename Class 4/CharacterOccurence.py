word = input("Please enter your own word: ")
character = input("Please enter your own character: ")
index = 0
occurrence = 0

while index < len(word):
    if word[index] == character:
        occurrence += 1
    index += 1

print("The total number of times", character, "has occurred =", occurrence)
