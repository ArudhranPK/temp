
def letter_by_letter(word):
    for i in range(1, len(word) + 1):
        print(" " * (len(word) - i) + word[i-1::-1])
    for i in range(len(word) - 1, 0, -1):
        print(" " * (len(word) - i) + word[i-1::-1])

inp = input("Enter a word to print the letters : ")
letter_by_letter(inp)
