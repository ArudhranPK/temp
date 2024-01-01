def sumDigit(num):
    if num < 10:
        return num
    else:
        return sumDigit(num % 10 + sumDigit(num // 10))
number = int(input())
print(sumDigit(number))
