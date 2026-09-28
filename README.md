# Student Management System

This project contains a simple Python-based Student Management System developed for academic purposes to practice and demonstrate fundamental Object-Oriented Programming (OOP) concepts.

## Purpose

The main purpose of this project is to understand and demonstrate how OOP concepts can be applied to a practical Student Management System.

The project manages different types of students and demonstrates classes, objects, attributes, methods, inheritance, polymorphism, method overriding, method overloading, and encapsulation.

## Project Structure

The system contains three main classes:

```text
Student
│
├── UndergraduateStudent
│
└── GraduateStudent
```

### Student

The `Student` class is the parent class. It contains common student information:

* Name
* Student ID
* Email
* Age
* Department
* Marks

It also contains methods to display student information, calculate results, and identify the student type.

### UndergraduateStudent

The `UndergraduateStudent` class inherits from the `Student` class.

Additional attribute:

* Semester

The class overrides the `get_student_type()` method to identify the student as an undergraduate student.

### GraduateStudent

The `GraduateStudent` class inherits from the `Student` class.

Additional attribute:

* Research Topic

The class overrides the `get_student_type()` method to identify the student as a graduate student.

## Features

* Stores student information.
* Displays student information.
* Calculates total marks.
* Calculates average marks.
* Assigns a grade based on the average.
* Supports undergraduate students.
* Supports graduate students.
* Demonstrates inheritance.
* Demonstrates polymorphism.
* Demonstrates method overriding.
* Demonstrates method overloading.
* Demonstrates encapsulation using private attributes.

## OOP Concepts Demonstrated

### Class and Object

Classes are created for students, and objects are created from those classes to represent individual students.

### Attributes

Student-related information such as name, student ID, email, age, department, semester, research topic, and marks are stored as attributes.

### Methods

Methods are used to perform different student-related operations, such as displaying information and calculating results.

### Inheritance

`UndergraduateStudent` and `GraduateStudent` inherit common properties and methods from the `Student` class.

### Polymorphism

The same method can be called on different student objects and produce different results depending on the type of student.

### Method Overriding

The `get_student_type()` method is overridden in both `UndergraduateStudent` and `GraduateStudent`.

### Method Overloading

The `calculate_result()` method uses `*args` so that it can work with different numbers of marks.

### Encapsulation

Private attributes such as `__email` and `__marks` are used to demonstrate data encapsulation.

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* Python classes and objects
* Inheritance
* Polymorphism
* Method overriding
* Method overloading
* Encapsulation

## Project Structure

```text
Student-Management-System/
│
├── student_management.py
│
└── README.md
```

### `student_management.py`

Contains the `Student`, `UndergraduateStudent`, and `GraduateStudent` classes along with their attributes, methods, objects, and program logic.

### `README.md`

Contains the project description, purpose, features, OOP concepts, and project structure.

## Setup and Run Instructions

### Prerequisites

Make sure Python is installed on your computer.

### Run the Project

Open a terminal and navigate to the project folder, then run:

```bash
python student_management.py
```

The program will create student objects and display their information and calculated results.

## Future Improvements

The project can be improved in the future by adding more functionality while keeping the OOP structure simple.

Possible improvements include:

* Add more student types.
* Add student search functionality.
* Add student update and delete options.
* Store multiple students.
* Add input validation.
* Add a menu-based interface.
* Store student information in a file or database.

## Academic Purpose

This project is created for academic purposes as part of Python programming practice. It demonstrates fundamental Object-Oriented Programming concepts through a simple Student Management System.

## Conclusion

The Student Management System provides a simple example of how Python OOP concepts can be used to organize and manage student information. It demonstrates how classes, inheritance, polymorphism, method overriding, method overloading, and encapsulation can work together in a practical project.

