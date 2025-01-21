sentence = input("Enter a sentence: ")
words = sentence.split()
max_length = 0  

for word in words:  
    length = len(word)  
    if length > max_length:  
        max_length = length

print()
print("Longest Word(s):")
for word in words:
    length = len(word)
    if length == max_length:  
        print(word)  
