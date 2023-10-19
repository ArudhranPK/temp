list1 = [('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]
print("Original list:")
print(list1)
dic = {}

for detail in list1:
    if detail[0] in dic:
        dic[detail[0]] += detail[1]
    else:
        dic[detail[0]] = detail[1]

max_name = ""
max_count = 0
for name in dic:
    if dic[name] > max_count:
        max_count = dic[name]
        max_name = name

print("\nMaximum aggregate value of the said list of tuple pair:")
print(f"('{max_name}', {max_count})")
