class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def birthday(self):
        self.age += 1
        print("Happy Birthday!")
people = []
morePeople = True
while (morePeople):
    fname, lname, age = input("Hello! What is your full name and age? ").split()
    person = Person(fname, lname, age)
    people.append(person)
    answer = input("Are there more people with you? (y/n): ")
    if (answer == "y"):
        morePeople = True
    else:
        morePeople = False
print("Nice to meet you,", people[0].fname, "and your", len(people) - 1, "friends.")