marks = []

for i in range(1, 6):
    marks.append([])
    
    for j in range(1, 6):
        while True:
            try:
                marks[i-1].append(float(input(f"Enter the subject {j} mark of student {i} : ")))
                break

            except:
                print("The input entered is not valid!!!!!\n")
    print()

total_avg = 0
for k in range(1, 6):
    print("The average marks of student", i, "is", sum(marks[k-1])/5)
    total_avg += sum(marks[k-1])/5

print("\nThe average marks of all five students is", total_avg/5)
