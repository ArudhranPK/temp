lis = ["PHP", "PHP", "Python", "PHP", "Python", "JS", "Python", "Python", "PHP", "Python"]

max_number = 0
max_word = ""

for word in lis:
    if lis.count(word) > max_number:
        max_word = word
        max_number = lis.count(word)

print(f"The most common element of said list is '{word}'.")