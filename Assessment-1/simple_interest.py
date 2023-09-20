def cal_simple_interest(amount, interest, time):
    return (amount * interest * time) / 100

while True:
    try:
        amou = float(input("Enter the princtipal amount : "))
        inte = float(input("Enter the rate of interest per year : "))
        time = float(input("Enter the time in years : "))
        si =  cal_simple_interest(amou, inte, time)
        print("\nThe simple interest for the given values is :", si)
        break
        
    except:
        print("The input entered is not valid!!!!!\n")