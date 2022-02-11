#include <iostream>
#include <string>
#include <vector>
class Person{
    std:: string fname, lname;
    int age;

    public:
    Person(std::string fname, std:: string lname, int age){
        this->fname = fname;
        this->lname = lname;
        this->age = age;


    }

    void Birthday() {

        this->age +=1;
        std::cout << "Happy Birthday!|\n";
    }
}

int maint() {
    std::vector<Person> people;
    bool morePeople = true;
    while morePeople{
        std::string fname, lname;
        int age:
        std::cout<< "Hello! What is your full name and age?"
        Person person(fname, lname, age);
        std::


    }


}