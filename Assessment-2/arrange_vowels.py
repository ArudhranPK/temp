words = []
for i in range(1, 11):
    words.append(input(f"Enter the string {i} : "))
words.sort()

for i in range(len(words)):
    for j in range(len(words) - i - 1):
        if len(words[j]) > len(words[j + 1]):
            words[j], words[j + 1] = words[j + 1], words[j]
print(words)
vowels = []
for word in words:
    count =  0
    for letter in word:
        if letter.lower() in "aeiou":
            count += 1
    vowels.append(count)
    
for i in range(len(vowels)):
    for j in range(len(vowels) - i - 1):
        if vowels[j] > vowels[j + 1]:

            vowels[j], vowels[j + 1] = vowels[j + 1], vowels[j]
            words[j], words[j + 1] = words[j + 1], words[j]

print(words)
print(vowels)