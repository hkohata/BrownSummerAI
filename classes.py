class Course:
    def __init__(self, type, size):
        self.type = type
        self.size = size

    def myfunc(self):
        print ("class type:" + self.type + " class")
        print ("class size:" + str(self.size) + " people")

c1 = Course("Math" , 50)
c1.myfunc()

class Student: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def fn(self):
        print("Student name: " + self.name)
        print ("Student age: "+ str(self.age))

s1 = Student ("Hugh" , 16)
s1.fn()

