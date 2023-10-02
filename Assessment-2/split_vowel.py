def split_vowels(word):
    output = ""
    for i in range(len(word)):
        if word[i].lower() in "aeiou":
            output += " " + word[i] + " "
        else:
            output += word[i]
    return output

words = []
for i in range(1, 11):
    words.append(input("enter the string {i} : "))

for word in words:
    print(split_vowels(word))