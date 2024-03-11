# collection are complex data types.
# differnet ways of storing data.
# lists - ordered, mutable, collection of values - [a, b, c....]
# dictionaries - unordered, mutable, collection is collection of key:value pairs. 
# - {"tolkien": value, "key": ["value_1", "value_2"], "key":....}
# tuples - ordered, immutable, collection of values (a, b, c) or no brackets = a, b, c
# sets - unordered, mutable, collection of unique values {value1, value2,...}

# lists are stored in a variable with []

#colours = ["blue", "green", "red", "yellow"]

#print(colours)

# referencing elements in a list by index location
# starts 0 and also end -1

#print(colours[0]) 
#print(colours[3]) 
#print(colours[-4])

# slicing - create a sub-list up to but not including the 2nd number.

#print(colours[0:2])
#print(colours[1:]) # no second number slices till the end of the list. 

# altering lists - use index position, need a value, delete with del:

#food = ["bread", "pasta", "apple", "pizza"]

#print(food)
#food[0] = "rice" # change directly without using a method.
#print(food) 

#del food[1]
#print(food)

# check if an item is in a list

#print("pizza" in food)
#print("orange" in food)

# nested lists

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1], combined[1][1])

# combined data types:

#my_list = ["red", 5, ["green", "blue"], 10.5]

#print(my_list[2][1])

# list methods:

# append:

#my_fruits = ["apple", "orange", "kiwi"]

#my_fruits.append("pear")
#print(my_fruits)

# remove

#my_fruits.remove("apple")
#print(my_fruits)

# insert - inserting at a specific place

#my_fruits.insert(0, "mango")
#my_fruits.insert(0, "grapes")
#print(my_fruits)

# extend (extend with a list)

#my_fruits.extend(["melon", "pomegranete"])
#print(my_fruits)

# reverse

#my_fruits.reverse()
#print(my_fruits)

# sort

#my_fruits.sort()
#print(my_fruits)

#my_fruits.sort(key=len)
#print(my_fruits)

# join

#x = ", ".join(my_fruits)
#print(x)
#print(type(x))

# dictionaries {} - key:value pairs
# similar to lists, but no indexing.
# keys have to be unique - values do not. 

drinks = {"fizzy": "sprite", "still": "water", "juice": "orange", "alcoholic": "wine"}

print(drinks)

# direct access:

print(drinks["still"]) # can only query with the keys of a dict. 

# add key:pair value to a dict.

drinks["non-alcoholic"] = "water"

print(drinks)

# overwrite

drinks["non-alcoholic"] = "squash"
print(drinks)

# returning values:

print(drinks.values())
print(drinks.keys())
print(drinks.items())

print("water" in drinks.values())

# get method

print(drinks.get("still"))
print(drinks.get("stille"))
print(drinks.get("stille", "not-found"))

# update method

drinks.update({"sugery": "cola"})
print(drinks)

# pop method

print(drinks.pop("non-alcoholic"))
print(drinks)

# make a dictionary of books, with 3 authors and multiple books per author.
# use an input asking for an author name.
# print to back as a STRING a list of the books by that author.
# use the .join method.

books = {"author_1": ["books1", "book2"], "author_2": ["book3", "book4"]}













