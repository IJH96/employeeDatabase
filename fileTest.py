from os.path import exists

#Created class
class Employee:
    def __init__(self, position, fname, lname, age, salary):
        self.position = position
        self.fname = fname
        self.lname = lname 
        self.age = age
        self.salary = salary
#Created array
people = []

#if statement for txt file
if (exists("employee.txt")):
    f = open("employee.txt")
    lines = f.readlines()
    for line in lines:
        position, fname, lname, age, salary = line.split()
        Employee = Employee(position, fname, lname, age, salary)
        people.append(Employee)
    f.close()
# Need to define all variables for the menu function
def addEmployee():
    position, fname, lname, age, salary = input("Enter the persons position, full name, age, and salary: ").split()
    Employee = Employee(position, fname, lname, int(age), int(salary))
    people.append(Employee)

def printPeople():
    for Employee in people:
        print(Employee.position, Employee.fname, Employee.lname, Employee.age, Employee.salary)

def RemoveEmployee():


def Raise():


def exit():




def printMenu():
    print("Select option:")
    print("    1. Show All Employees")
    print("    2. Add a employee")
    print("    3. Remove a employee")
    print("    4. give promotion/raise")
    print("    5. Exit program")


keepRunning = True
while (keepRunning):
    printMenu()
    selection = input("Enter selection: ")
    if (selection == "1"):
        printPeople()
    elif (selection == "2"):
        addPerson()
    elif (selection == "3"):
        #removeEmployee()
    elif (selection == "4")
        #giveRaise()
    elif (selection == "5")
        keepRunning = False
        f = open("fileTest.txt", "w")
        for person in people:
            f.write(str(person.fname) + " " + str(person.lname) + " " + str(person.age) + "\n")
        f.close()
    else:
        #print("Not Possible")
        #return printMenu()