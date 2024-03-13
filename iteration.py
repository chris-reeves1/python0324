# iteration is another word for loops.
# repeating blocks of code over and over.
# saves time, avoids having to write our code multiple times.

# 2 types of loops - while and for

# while loops
# a while loop continuously executes code whilst a condtion is true.
# or when another condition is met and the loop break. 
# if a condiotion is never true the while loop will never start. 

#print("1")
#print("2")
#print("3")
#print("4")

#x = 0

#while x < 101:
#    print(x)
#    x += 1

# break 

#i = 1

#while i < 6:
#    if i == 3:
#        break
#    print(i)
#    i += 1

# continue

#j = 0 

#while j < 6:
#    j += 1
#    if j == 3:
#        continue
#    print(j)

# while true - must have a clearly defined way of breaking.

#while True:
#    name = input("enter your name: ")
#    if name == "quit":
#        break
#    else:
#        print(f"hello {name}")

# for loops
# a for loop will iterate over any collection - lists/strings/dictionaries/sequences
# useful for when we want to use the data in a collection.abs

# iterating through lists

#my_fruits = ["apple", "orange", "pear"]

#for fruit in my_fruits:
#    print(fruit)

#numbers = [1, 2, 3, 4]

#for item in numbers:
#    print(item)

# in a while loop:

#l = 0

#while l < len(numbers):
#    print(numbers[l])
#    l += 1

 # range

#for a in range(5):
#    print(a)

#for a in range(1,5):
#    print(a)

#for a in range(1, 10, 2):
#    print(a) # high number not included, this example goes up in steps of 2. 

# stings

#for letter in "hello":
#    print(letter)

#for word in "hello world".split():
#    print(word)

# list comprehension:
#      expression-item---iterable
#result = [x**2 for x in range(5)]
#print(result)

#result = []

#for x in range(5):
#    result.append(x**2)

#print(result)

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# --------------------------------------------- finally a conditional.
#even_numbers = [number**2 for number in numbers if number % 2 == 0]
#print(even_numbers)

# dictionaries

#for i in {"drink":"wine"}:
#    print(i)

#for i in {"food":"jam"}.values():
#    print(i)

#for i in {"shape": "square"}.items():
#    print(i)

# break 

#for i in range(10):
#    if i == 5:
#        break
#    print(i)

# nested loop:

#for i in range(1,3):
#    for j in range(1,4):
#        print(i, "x", j, "=", i*j)

# challenge:
# write a loop that asks for 5 names (as user input) 
# and for each one prints name + is great.

# while loop
# for loop
# list comprehension + print statement
# stretch (optional) - list comprehension ONE LINE OF CODE ONLY!!!!

# set up repo send me link.
# then do labs 2, 3 and 4.

# while loop

#counter = 0

#while counter < 5:
#    name = input("enter a name: ")
#    print(name + " is awesome")
#    counter += 1

# for loop


#for counter in range(5):
#    name = input("enter a name: ")
#    print(name + " is awesome")


# list comprehension

#names = [input("what is your name?: ") for name in range(5)]
#for name in names:
#    print(f"{name} is awesome")

#[print(f"{name} is awesome") for name in [input("enter a name: ") for x in range(5)]]


#Morning Challenge - rewrite this code without using if statements 
#(or max or any inbuilt functions!!)

#num = 10
#num_1 = 20

#if num > num_1:
#    print(num)

#else:
#    print(num_1)

#num1 = 12
#num2 = 10


#largest = num1 * (num1 > num2) + num2 * (num2 > num1)

#print(f"{largest} is the largest number")



