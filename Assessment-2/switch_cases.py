def switch_case(word):
    output = ""
    for letter in word:
        if letter.islower():
            output += letter.upper()
        elif letter.isupper():
            output += letter.lower()
        else:
            output +=  letter
    return output

words = []
for i in range(1, 11):
    words.append(input(f"Enter the string {i} : "))
print()

for word in words:
    print(switch_case(word))