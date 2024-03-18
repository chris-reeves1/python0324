# modules

# modules are just files, that we use to extend our functionality.
# we can import existing modules or just use our own.
# many modules are built in to python, and do not require any set up.
# some need to be installed - pip is the package manager. 
# pypi.org

#import math # imports the entire module.

#number = 10

#answer = math.sqrt(number) # modulename.method(args)

#print(answer)

#import math
#import random

#def random_pi():
#    return math.ceil(random.randint(1,10) * math.pi)

#for i in range(5):
    #print(random_pi())

# just with desired objects to save memory

#from math import pi, ceil, floor
#from random import randint

#def random_pi():
    #return floor(randint(1,10) * pi)

#for i in range(1,10):
    #print(random_pi())

# exercise
# create 2 files, one called dice.py - write a function that will 
# generate a random number between 1 and 6. in the second file use the dice 
# module to simulate throwing 2 dice and print its output. 


# files

# importance of file handling:
# storing and retrieving data.
# configuring systems
# sharing for data between apps/software
# logs

# read, write, edit files
# most file types are supported, some will need to import modules.

# lets focus on txt files:

# read mode ("r"): Defualt mode, used for reading a file. 
# write mode ("w"): opens a file for writing, create a file if it doesnt exist. 
# append mode ("a"): opens for writing, will create a new file, appends to the end of the file.
# binary - add a b -eg ("rb", "wb") for binary fils.

# eg:

#file = open("filename", "mode") # var to store, open. 

#file.close() # must remeber to close a file after use. Most recently open
# file will close. 

# reading from a file

# read() read the entire file
# readline() read the next line from the file
# readlines() reads all the lines puts them in a list.
# seek() go to a line. default to 1st line otherwise pass a line as an arg.

# writing a file
# write() used to write string to the file.
# writelines() write a list to the file.

#file = open("lines.txt", "r")

#lines = file.readlines()

#print(lines)

#file.close()

#file = open("lines1.txt", "w")

#for n in range(1, 11):
#    newline = "this is a new line" + " " + str(n) + "\n"
#    file.write(newline)

#file.close()

#file = open("lines1.txt", "r")

#outfile = ""

#for line in range(1, 10):
#    if line % 2 == 0:
#        outfile += file.readline()
#    else:
#        file.readline()

#file = open("lines1.txt", "w")

#file.write(outfile)

#file.close()

# exercise
# open a new text file (w mode) called teams.txt - add the names of 5 sports teams.
# read and display the names of the 1st and 4th team (.strip())
# edit the file so that the top line is replaced with "this is a new line"
# print out the edited file line by line. 

# making file and content

file = open("teams.txt", "w")

sports_teams = ["man utd", "man city", "barcelona", "real madrid", "psg"]

for i in sports_teams:
    newline = i + "\n"
    file.write(newline)

file.close()

file = open("teams.txt", "r")

# printing lines 1 and 4

lines = file.readlines()

print(lines[0].strip())
print(lines[3].strip())

file.close()

# editing the first line
file = open("teams.txt", "r")

lines = file.readlines()
file.close()

lines[0] = "this is a new line"

file = open("teams.txt", "w")
for i in range(len(lines)):
    if i == len(lines)-1:
        file.write(lines[i])
    else:
        file.write(lines[i].strip() + "\n")

file.close()

file = open("teams.txt", "r")

for line in file:
    print(line.strip())
file.close()


# with

with open("filename.txt", "mode") as file: # alias
    for n in range(1,11):
        newline = ........
        file.write(newline)










