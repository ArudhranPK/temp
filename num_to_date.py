def findLeapYear(year):
    if year % 400 == 0 and year % 100 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def findMonth(month):
    if month == 1:
        return "Jan"
    elif month == 3:
        return "Mar"
    elif month == 4:
        return "Apr"
    elif month == 5:
        return "May"
    elif month == 6:
        return "Jun"
    elif month == 7:
        return "Jul"
    elif month == 8:
        return "Aug"
    elif month == 9:
        return "Sep"
    elif month == 10:
        return "Oct"
    elif month == 11:
        return "Nov"
    else:
        return "Dec"

while True:
    date = input("Enter a date number in the form DDMMYYYY : ")

    if date.isnumeric() and len(date) == 8:
        day = int(date[0:2])
        month = int(date[2:4])
        year = int(date[4:])

    else:
        print("\nThe entered number is not in the format\n")
        continue

    if month > 12:
        print("\nThe entered month exceeds 12\n")
        continue
    else:
        if year > 2050:
            print("\nThe entered year exceeds 2050\n")
            continue

        else:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if day < 32:
                    break
                else:
                    print("\nThe entered date exceeds 31 days for the entered month\n")
                    continue
                
            elif month in [4, 6, 9, 11]:
                if day < 31:
                    break
                else:
                    print("\nThe entered date exceeds 30 days for the entered month\n")
                    continue
            
            else:
                if findLeapYear(year):
                    if day < 30:
                        print(f"{day} Feb {year}")
                        break
                    else:
                        print("\nThe entered year is leap year.\nThe date exceed 29 days of February\n")
                        continue
                else:
                    if day < 29:
                        print(f"{day} Feb {year}")
                        break
                    else:
                        print("\nThe date exceeds 28 days of February\n")
                        continue

print(f"{day} {findMonth(month)} {year}")