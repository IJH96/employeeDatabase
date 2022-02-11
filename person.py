
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname 
        self.age = age
    def birthday(self):
        self.age +=1
        print("Happy Birthday!")