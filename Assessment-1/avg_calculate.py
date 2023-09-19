marks = []
for i in range(1, 6):
    for j in range(1, 6):
        while True:
            try:
                marks[i-1][j-1] = float(input("Enter the  subject", j,  "mark of student", i, ": "))

            except:
                print("The input entered is not valid!!!!!\n")