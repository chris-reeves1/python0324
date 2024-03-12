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

temp = 28

if temp >= 30:
    print("its very hot")
elif temp > 25: 
    print("pretty hot")
elif temp > 20:
    print("its ok")
elif temp > 10:
    print("cold")
else:
    print("genrally bad")

# exercise
# user input for a grade/mark
# if the mark is greater than 85 print 'distinction'
# if the mark is between 65 and 85 print pass
# anything else print 'fail'
# if elif else - if if else 