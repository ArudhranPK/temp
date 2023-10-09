words = input("Enter the string : ").split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

max_word = ""
max_number = 0

for word in freq:
    if freq[word] > max_number:
        max_number = freq[word]
        max_word = word

print(f"\nThe most repeated word is '{max_word}' for {max_number} times.")