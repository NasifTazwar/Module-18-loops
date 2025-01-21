sentence = input("Please enter a sentence: ")
word_count = 1

for i in range(len(sentence)):
    if sentence[i] == ' ':
        word_count += 1

print("Total Number of Words in this String =", word_count)
