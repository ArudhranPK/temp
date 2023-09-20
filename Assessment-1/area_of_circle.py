pi = 3.14159

while True:
    try:
        radius = float(input("Enter the radius of the circle : "))
        area = pi * radius ** 2
        print("The area of the circle is", area, "sq. units")
        break

    except:
        print("\nThe input entered is not valid!!!!!\n")