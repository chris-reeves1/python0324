# if, elifs, elses
# allows different pathways for our code to take.

#my_bool = False

#if my_bool:
#    print("my_bool is true")
#else:
#    print("mybool is false")

#is_admin = False
#is_verified = True 
#on_holiday = False

#if (is_admin or is_verified) and not on_holiday:
#    print("access granted")
#else:
#    print("access denied")

#if some-condition:
#    .....
#    if:
#        .....
#    else:
#        ......
#else:
#    .....

# conditional operators:

# equals to: ==
# not to equals to: !=
# less than: <
# more than: >
# less than or equals to <=
# more than or equals to >=


#money = 10

#if money >= 10:
#    print("i have some money")
#else:
#    print("i dont have much money")

# elif - else if
# only triggers if no other conditionals have evaluated to being true.
# mostly only 1 statement is true - using elifs wil make our code more efficient.

#temp = 28

#if temp >= 30:
#    print("its very hot")
#elif temp > 25: 
#    print("pretty hot")
#elif temp > 20:
#    print("its ok")
#elif temp > 10:
#    print("cold")
#else:
#    print("genrally bad")

# exercise
# user input for a grade/mark
# if the mark is greater than 85 print 'distinction'
# if the mark is between 65 and 85 print pass
# anything else print 'fail'
# if elif else - if if else

#x = int(input("enter grade: "))

#if x >= 85:
#    print("distinction")
#elif x >= 65:
#    print("pass")
#else:
#    print("fail")

# multiple compatators (multiple condtions using and/or):

#deposit = 101
#password = "password1"

#if 0 < deposit <= 100 or password == "password1":
    #print(f"thankyou for deposit of {deposit}")
#else:
    #print("failed to deposit")

# and takes precedence over or!!!

#if not 0 < deposit <=100 or password != "password":
    #print("failed to deposit")
#else:
    #print("deposit ok")

# in and not in:

#name = "root123"

#if name in ("root", "admin", "user"):
#    print("invalid username")
#else:
    #print("accepted")

#if name not in ("root", "admin", "user"):
#    print("accepted")
#else:
#    print("invalid")

# weight converter app - 
# user input for weight (float)
# user to select either kgs or lbs.
# if statement to check unit entered.
# logic to convert from kgs to lbs and lbs - kgs
# print out converted value.
# error handling for upper/lower
# optional - input validation

#1st solution

#weight = float(input("enter weight: ")) 
#unit = input("enter K for (kgs) or L for (lbs): ")

#if unit.upper() == "K":
#    converted = weight / 0.45
#    print(f"weight in lbs: {converted}")
#elif unit.upper() == "L":
#    converted = weight * 0.45
#    print(f"weight in Kgs: {converted}")
#else:
#    print("invalid unit pls enter k or l")
    
# 2nd solution
import sys

try:
    weight = float(input("enter weight: "))
except ValueError:
    print("invalid input. Please enter a numeric value for weight!!")
    sys.exit()

while True:
    unit = input("enter K for (kgs) or L for (lbs): ").upper()
    if unit == "K":
        converted = weight / 0.45
        print(f"weight in lbs: {converted}")
        break
    elif unit == "L":
        converted = weight * 0.45
        print(f"weight in Kgs: {converted}")
        break
    else:
        print("invalid unit pls enter a k or l!!!!!!")












