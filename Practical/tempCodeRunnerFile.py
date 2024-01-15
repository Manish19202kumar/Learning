class Student:
    def _init_(self, rollno, name, class_name):
        self.rollno = rollno
        self.name = name
        self.class_name = class_name

    def display(self):
        print(f"Roll No: {self.rollno}")
        print(f"Name: {self.name}")
        print(f"Class: {self.class_name}")


student_list = []

def add_student():
    rollno = input("Enter Roll No: ")
    name = input("Enter Name: ")
    class_name = input("Enter Class: ")

    student = Student(rollno, name, class_name)
    student_list.append(student)
    print("Student added successfully!")


def display_students():
    if not student_list:
        print("No students found.")
    else:
        print("\nList of Students:")
        for student in student_list:
            student.display()
            print()


while True:
    print("\n===== Student Information System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")