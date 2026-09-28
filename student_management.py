class Student:
    def __init__(self, name, student_id, email, age, department, marks=None):
        self.name = name
        self.student_id = student_id
        self.__email = email  # Encapsulation
        self.age = age
        self.department = department
        self.__marks = marks if marks is not None else []

    def display_info(self):
        print("\n--- Student Information ---")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.__email}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Student Type: {self.get_student_type()}")

    # Method overloading using *args
    def calculate_result(self, *marks):
        if marks:
            self.__marks = list(marks)

        if not self.__marks:
            return "No marks available."

        total = sum(self.__marks)
        average = total / len(self.__marks)

        if average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        return f"Total: {total}, Average: {average:.2f}, Grade: {grade}"

    def get_student_type(self):
        return "General Student"


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester, marks=None):
        super().__init__(name, student_id, email, age, department, marks)
        self.semester = semester

    # Method overriding
    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Semester: {self.semester}")


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic, marks=None):
        super().__init__(name, student_id, email, age, department, marks)
        self.research_topic = research_topic

    # Method overriding
    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")


# -------------------------------
# Creating Objects
# -------------------------------

student1 = UndergraduateStudent(
    "Ayesha Rahman",
    "UG001",
    "ayesha@example.com",
    20,
    "Computer Science",
    5
)

student2 = GraduateStudent(
    "Rahim Ahmed",
    "GR001",
    "rahim@example.com",
    25,
    "Computer Science",
    "Artificial Intelligence"
)

# Polymorphism
students = [student1, student2]

for student in students:
    student.display_info()
    print(student.calculate_result(85, 78, 92))
    print()