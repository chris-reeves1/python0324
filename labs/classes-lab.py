# task2 

class Students:
    def __init__(self, name, age, class_="maths"):
        self.name = name
        self.age = age
        self.class_ = class_

    def average_test_score(self, scores):
        total_score = sum(scores)
        average_percentage = total_score / (len(scores) * 100) * 100
        return f"{self.name} - average test score is {average_percentage}"

student_1 = Students("John", 10)

print(student_1.average_test_score([20, 60, 60]))


# task3

class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} cm")

    def __str__(self):
        return f"{self.name} {self.__class__.__name__}, {id(self)}, {self.__dict__}"

class Owl(Bird):
    
    nocturnal = True
    
    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)

    def hoot(self):
        print(f"{self.name} is hooting")

    def __str__(self):
        return super().__str__() + f"- nocturnal: {self.nocturnal}"

class Dodo(Bird):

    extinct = True

    def __init__(self, name, wingspan):
        super().__init__(name, wingspan)
    
    def fly(self):
        print(f"{self.name} doesnt fly")

    def __str__(self):
        return super().__str__() + f"- extinct: {self.extinct}"


bird1 = Bird("eagle", 20)
owl1 = Owl("barn owl", 90)
dodo1 = Dodo("the dodo", 120)

bird1.fly()
print(bird1)

owl1.fly()
owl1.hoot()
print(owl1)

dodo1.fly()
print(dodo1)











