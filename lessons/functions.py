# functions - a block of code that either performs a task or returns a value.
# repeatability. 


#def greet(name): # parameters take in agruments.
#    print(f"hi {name}")

#greet("chris")

#def greet_1(first_name, second_name, age):
#    print(f"{first_name} {second_name} is {age}")

#greet_1(30, "reeves", "ghh")

# better to use return as we can store in a variable.
# store in a file.
# print and input limits our functionality. 

# return

#def greeter(name):
#    return (f"hello {name}")

#x = greeter("chris")

#print(x)

#def greet_3(name, age=10): # defualt args must come as last arguments.
#    return (f"{name} is {age}")

#print(greet_3("chris"))
#print(greet_3("john", 20)) 

# exercise - make a function that does addition of 2 numbers that we pass as args.

#def add_calc(num1, num2):
#    return num1 + num2

#print(add_calc(5,5))


# *args
# used if we dont know how many args will be passed through.
# we add a * before the parameter.
# it will recieve a tuple of arguments. 


#def fruit_list(*fruits):
 #   print("the fruits are:")
 #   for fruit in fruits:
 #       print(fruit)

#fruit_list("orange", "pear", "apple")

#def numbers_list(*numbers):
 #   for i in numbers:
 #       print(i)

#numbers_list(1, 2, 3, 4, 5, 6, 7, 8, 9)

#def make_pizza(size, *toppings):
#    print(f"order for {size}-inch-pizza with the following toppings:")
#    for topping in toppings:
#        print(f"- {topping}")#

#make_pizza(12, "mushrooms", "green peppers")

# kwargs - keyword arguments
# send args as key/value pairs
# order therfore does not matter.

#def fruit_list(fruit1, fruit2, fruit3):
#    print(f"fav fruit = {fruit1}")
#    print(f"2nd fav fruit = {fruit2}")
#    print(f"3rd fav fruit = {fruit3}")

#fruit_list(fruit1="apple", fruit3="orange", fruit2="pear")

# **kwargs
# if we dont know how many kwargs there wil be.

#def fav_food(**food):
#    print("fav food is", food["fruit"], "not", food["dessert"])

#fav_food(dessert="ice-cream", fruit="apple", dairy="milk")

# / - a marker dividing positional-only parameters from the rest. 
# before / the parameters must be in order and not named. 

#def example(a, b, /, c, d):
#    print(f"a = {a}, b = {b}, c = {c}, d = {d}")

#example(1, 2, d=3, c=4)

# passing a list as an arg

#def my_function(food):
#    for x in food:
#        print(x)

#list1 = ["apple", "pear", "orange"]

#my_function(list1)

# format 

name = "john"
age  = 20
height = 1.7

#print("my name is {}, i am {}, my height is {}".format(name, age, height))

x = "my name is {}, i am {}, my height is {}"

print(x.format(name, age, height))




















































