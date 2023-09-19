def cal_simple_interest(amount, interest, time):
    return (amount * interest * time) / 100

while True:
    try:
        amou = float(input("Enter the princtipal amount : "))

        while True:
            try:
                inte = float(input("Enter the rate of interest per year : "))

                while True:
                    try:
                        time = float(input("Enter the time in years : "))
                        print("\nThe simple interest for the given values is :", cal_simple_interest(amou, inte, time))
                        break
                
                    except:
                        print("The input entered is not valid!!!!!\n")
                break

            except:
                print("The input entered is not valid!!!!!\n")
        break

    except:
        print("The input entered is not valid!!!!!\n")