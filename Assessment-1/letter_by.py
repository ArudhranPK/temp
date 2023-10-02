#def letter_by_letter(word):
#    for i in range(1, len(word) + 1):
#        print(word[0:i:])
#    for i in range(len(word) - 1, 0, -1):
#        print(word[0:i:])

def letter_by_letter(word):
    for i in range(1, len(word) + 1):
        print(" " * (len(word) - i) + word[0:i:])
    for i in range(len(word) - 1, 0, -1):
        print(" " * (len(word) - i) + word[0:i:])

inp = input("Enter a word to print the letters : ")
letter_by_letter(inp)
