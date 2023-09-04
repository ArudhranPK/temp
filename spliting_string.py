inp = str(input("Enter the string to seperate : "))
letters, numbers, other = "", "", ""

for char in inp:
    if char.isalpha():
        letters += char
    elif char.isnumeric():
        numbers += char
    else:
        other += char

print(f"\nThe letters in the given string is [{letters}]")
print(f"The numbers in the given string is [{numbers}]")
print(f"The other characters in the given string is [{other}]")