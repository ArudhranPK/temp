while True:
    try:
        f = float(input("Enter temprature in Fahrenheit : "))
        c = (f - 32) * (5 / 9)
        print("The temprature in Celcius is", c, "degrees.")
        break
        
    except:
        print("The input entered is not valid!!!!!\n")
