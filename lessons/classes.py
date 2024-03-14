# classses is part of OOP (objected orientated programming)
# key concepts:
# class - a blueprint - of attributes (vars/arg) and methods (functions)
# we can use the class against an object.abs
# object - an instance of a class.
# allow to easily make multiple objects of the same type.

#class Dog: # create class called dog.abs
    #energy = "high" # setting an attribute of the class.

    #def speak(self): #creating a method
        #print("bark")

#fido = Dog() # makes an object called fido of the Dog class

#fido.energy = "low"
#print(fido.energy)

#fido.speak()

#class Student():
#    pass

#student1 = Student()
#student2 = Student()

#print(student1)

#student1.first = "john"
#student1.last = "smith"
#student1.age = 10

#print(student1.age, student1.first)

#class Student():
#    def __init__(self, first, last, age): # dunder - indictaes a background task. 
#        self.first = first # init method initialises the object with these attributes.
#        self.last = last # the self param refers to the object itself. 
#        self.age = age # self mpas the class data to the object. 

#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "smith", 12)

#print(student1.age, student2.age)

#class Student():
#    def __init__(self, first, last, age): # dunder - indictaes a background task. 
#        self.first = first # init method initialises the object with these attributes.
#        self.last = last # the self param refers to the object itself. 
#        self.age = age # self mpas the class data to the object. 
#        self.full = first + " " + last


#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "smith", 12)

#print(student1.full, student2.full)

#class Student():
  #  def __init__(self, first, last, age): # dunder - indictaes a background task. 
  #      self.first = first # init method initialises the object with these attributes.
 #       self.last = last # the self param refers to the object itself. 
 #       self.age = age # self mpas the class data to the object. 

#    def fullname(self):
#        return(self.first + " " + self.last)


#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "smith", 12)

#print(student1.fullname())
#print(Student.fullname(student2))

# change an attribute with a method

#class Student():
#    def __init__(self, first, last, age): # dunder - indictaes a background task. 
#        self.first = first # init method initialises the object with these attributes.
#        self.last = last # the self param refers to the object itself. 
#        self.age = age # self mpas the class data to the object. 

#    def fullname(self):
#        return(self.first + " " + self.last)

#    def change_age(self):
#        self.age = int(self.age + 1)

#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "smith", 12)

#print(student1.age, student2.age)

#student1.change_age()
#student2.change_age()

#print(student1.age, student2.age)

# self-class variable

#class Student():

   # age_increase_amount = 25

    #def __init__(self, first, last, age): # dunder - indictaes a background task. 
     #   self.first = first # init method initialises the object with these attributes.
     #   self.last = last # the self param refers to the object itself. 
     #   self.age = age # self mpas the class data to the object. 

    #def fullname(self):
      #  return(self.first + " " + self.last)

 #   def change_age(self):
 #       self.age = int(self.age + self.age_increase_amount)

#student1 = Student("john", "smith", 10)
#student2 = Student("katy", "smith", 12)

#print(student1.age)
#student1.change_age()
#print(student1.age)

#print(student1.age_increase_amount)
#print(student2.age_increase_amount)

# __dict__

#print(student1.__dict__)
#print(student2.__dict__)
#print(Student.__dict__)

# change to the variable

#Student.age_increase_amount = 20
#print(Student.__dict__)

#student1.age_increase_amount = 10

#student1.change_age()
#print(student1.age)

#print(student1.__dict__)
#print(student2.__dict__)
#print(Student.__dict__)

# non-self class variable

class Student():

    age_increase_amount = 25
    num_of_students = 0 


    def __init__(self, first, last, age): # dunder - indictaes a background task. 
        self.first = first # init method initialises the object with these attributes.
        self.last = last # the self param refers to the object itself. 
        self.age = age # self mpas the class data to the object. 

        Student.num_of_students += 1

    def fullname(self):
        return(self.first + " " + self.last)

    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

print(Student.num_of_students)
student1 = Student("john", "smith", 10)
print(Student.num_of_students)
student2 = Student("katy", "smith", 12)
print(Student.num_of_students)

#class Animal:
  #  def __init__(self, name, species):
  #      self.name = name
  #      self.species = species

 #   def eat(self):
 #       print(f"{self.name} is eating")

#class Cat(Animal):
    #def __init__(self, name, species, breed):
        #super().__init__(name, species)
        #self.breed = breed#

#    def meow(self):
#        print("meow")

#my_cat = Cat("w", "f", "g")

#my_cat.meow()
#my_cat.eat()

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.name} - {self.species} - {self.__class__.__name__}"

class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

    def __str__(self):
        return super().__str__() + f"- {self.breed}"

my_cat = Cat("w", "f", "g")

print(my_cat)