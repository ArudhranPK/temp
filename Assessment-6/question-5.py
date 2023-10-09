dictionary = {"Afghanistan" : 93, "Albania" : 355, "Algeria" : 213, "Andorra" : 376, "Angola" : 244}

ordered = sorted(dictionary)
print("In assending order:")
for name in ordered:
    print(f"{name} {dictionary[name]}")

ordered = sorted(dictionary, reverse = True)
print("\nIn reverse order:")
for name in ordered:
    print(f"{name} {dictionary[name]}")