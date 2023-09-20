def fahrenheit_to_celsius(temprature):
    return (temprature - 32) * (5 / 9)

while True:
    try:
        temp = float(input("Enter temprature in Fahrenheit : "))
        print("The temprature in Celcius is", fahrenheit_to_celsius(temp), "degrees.")
        break
        
    except:
        print("The input entered is not valid!!!!!\n")
