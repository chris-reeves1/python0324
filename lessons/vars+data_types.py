# variables - a reference (a name), a selection of memory
# protected - cant be altered unless called by name (memory reserved).

#age = 30
#x = "30" 

# naming convention - names should be descriptive, lowercase, never start with a number.
# pep-8 style guide.
# follow team style and be consistant. 

# Var = 12 # Dont start with a capital letter.
# 1var = 12 # cant start with number
# VAR = 20 - convention for constants, things we dont want to change. eg; "DEBUG = true"
# print = 30 -  avoid python inbuilt keywords.abs

# variable scope:

#global_variable = "accessible everywhere"

#def function():
#    local_variable = "accessible only in this function"
#    print(global_variable) # this will work
#    print(local_variable) # this will also work

#print(local_variable) # This will raise an error. 

# person_one_age = 10 - snake case
# personOneAge = 10 - camel case

# in-built functions

#print("prints to standard output")
#type(shows data type of var)
#input(allows input on standard input)

# data types

# x = 10 (int)
# y = "hello" (string)
#z = False - bool - true or false, something or nothing, 1 or 0. 
#a = True - bool 
#v = 10.2545555 float (decimal number)

#x = "True"
#print(type(x))

#name = input("what is your name? ") # input defaults to a str. 
#age = int(input("what is your age? ")) # casts as an integer. 

# string concatination 
#print("your name is " + name)
#print("your name is", name, "your age is", age)
#print(f"your name is {name}, your {age} years old") # f-sting allows diff data types to be formatted in a str. 

#name1 = "rex"
#age = 2
#bark = True
#meow = False

#print(name, "barks:", bark)

# escape chars

# \\ - backslash , \n - newline, \t -  tab, \u unicode,\U extended unicode. 

#print("person 1: \tHey how are you?\nPerson 2: \tGood thanks \U0001F604")

# string methods:

#print("hELLo WorLD".lower())
#print("hello world".upper())

#print("hello world".replace("world", "class"))
#print("hello world".count("o"))
#print("hellow world".split().upper())

# bodmas

# brackets
# order of
# division
# multiplication
# addition
# subtraction

# + - / *
# floor division - // eg; 10//3 = 3 
# modulo - % eg;  10%3 = 1
 
#length = int(input("enter the length of rectangle"))
#width = int(input("enter the width of the rectangle"))

#perimerter = 2 * (length + width)

#print(f"perimeter is {perimerter}")






