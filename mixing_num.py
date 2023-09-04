while True:
    num1 = input("Enter a number : ")
    num2 = input("Enter a number with same number of digits as before : ")

    if len(num1) == len(num2):
        break
    else:
        print("\nThe entered numbers doesn't have same number of digits.\nPlease try again.\n")

output = "\n"
for i in range(len(num1)):
    output += f"{num1[i]}{num2[i]}"

print(output)