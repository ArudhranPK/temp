dict1 = {"R": "Red", "B": "Black", "P": "Pink"}
dict2 = {"G": "Green", "W" : "White"}
dict3 = {"O" : "Orange", "W" : "White", "B" : "Black"}

dict_out = {}

print("The original dictionaries : ")
print(dict1)
print(dict2)

print("\nMerged dictionary : ")
dict_out.update(dict1)
dict_out.update(dict2)
print(dict_out)

print("\nThe original dictionaries : ")
print(dict1)
print(dict2)
print(dict3)

print("\nMerged dictionary : ")
dict_out.update(dict3)
print(dict_out)