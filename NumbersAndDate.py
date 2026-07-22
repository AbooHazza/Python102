import math

def mathcalc(number):

    real = round(number)
    power = pow(real, 2)
    square = math.sqrt(power)
                                        # reminder = math.remainder(number)
    return real, power, square 

def main():
    x = float(input("! Enter Number: "))
    print("=============== real / power/ square ==================")
    print(mathcalc(x))
    print("=============== reminder ==================")
    y = int(input("! Enter The The Number You Want to divade on it: "))
    print(math.remainder(x,y))
main()

# genrate a random number between(1 , 99)
import random

print(random.randint(1 , 99)) 

# datetime
import datetime as dt

MoyedDOB = dt.date(2006,9,27)
print(MoyedDOB)
MoyedTIME = dt.time(6,30,00)
print(MoyedTIME)
print(MoyedTIME.hour)
print(MoyedTIME.minute)
print(MoyedTIME.second)
now = dt.datetime.today()
print(now)   # now.year.month.day.hour.minute.second
print(now.strftime('%A %B %Y')) #time to string 



