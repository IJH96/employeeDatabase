from os.path import exists
import sys 
#imported Stuff

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
        employee = Employee(position, fname, lname, age, salary)
        people.append(employee)
        f.close()

# Need to define all variables for the menu function
def addEmployee():
    position, fname, lname, age, salary = input("Enter the persons position, full name, age, and salary: ").split()
    employee = Employee(position, fname, lname, int(age), int(salary))
    people.append(employee)

def printPeople():
    i=1
    for employee in people:
        print(i, employee.position, employee.fname, employee.lname, employee.age, employee.salary)
        i+=1

def removeEmployee():
    printPeople()
    empNumber = int(input("Enter employee to remove from menu: "))
    people.pop(empNumber-1)

    

def Raise():
    printPeople()
    empNumber = int(input("Enter number of employee to give raise: "))
    new_Pay = float(input("enter new pay rate: "))
    change_title = input("Does the raise come with a change in job title (y/n): ")
    if (change_title == "y"):
        position = input("Enter new position: ")
        people[empNumber-1].position = new_title

    
    


def exit():
    print("Menu closing")
    sys.exit()



def printMenu():
    print("Select option:")
    print("    1. Show All Employees")
    print("    2. Add a employee")
    print("    3. Remove a employee")
    print("    4. give promotion/raise")
    print("    5. Exit program")
    print("    6. Another exit that I wanted to try")

#Create while loop
keepRunning = True
while (keepRunning):
    printMenu()
    selection = input("Enter selection: ")
    if (selection == "1"):
        printPeople()
    elif (selection == "2"):
        addEmployee()
    elif (selection == "3"):
        removeEmployee()
    elif (selection == "4"):
        Raise()
    elif (selection == "5"):
        keepRunning = False
        f = open("fileTest.txt", "w")
        for person in people:
            f.write(str(person.fname) + " " + str(person.lname) + " " + str(person.age) + "\n")
        f.close()
    elif (selection == "6"):
        exit()

    else:
        print("Not Possible")
    

