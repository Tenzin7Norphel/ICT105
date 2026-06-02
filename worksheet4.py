def course_enrollment(student_id, first_name, last_name,
                      course_id, course_name, action="Echo"):

    print(
        f"{action}: Student {student_id} - {first_name} {last_name} "
        f"is enrolled in {course_id} - {course_name}"
    )


# Positional arguments
course_enrollment(
    1001,
    "Alice",
    "Smith",
    "CS101",
    "Introduction to Computer Science"
)

# Keyword argument
course_enrollment(
    student_id=1002,
    first_name="Bob",
    last_name="Johnson",
    course_id="MATH101",
    course_name="Calculus I",
    action="Add"
)

# Amend
course_enrollment(
    1003,
    "Charlie",
    "Brown",
    "PHY101",
    "General Physics I",
    "Amend"
)

# Delete
course_enrollment(
    1004,
    "David",
    "Lee",
    "CHEM101",
    "General Chemistry I",
    "Delete"
)

def collect_courses():
    courses = []

    for i in range(4):
        course = input(f"Enter course {i+1}: ")
        courses.append(course)

    return courses


def student_summary(student_id, student_name):

    courses = collect_courses()

    semester = input("Enter semester: ")
    year = input("Enter year: ")

    print("\nEnrollment Summary")
    print("Student ID:", student_id)
    print("Student Name:", student_name)
    print("Courses:", courses)
    print("Semester:", semester)
    print("Year:", year)


student_summary(1001, "Alice Smith")

def store_courses(**courses):

    print("Course Dictionary")

    for course_id, course_name in courses.items():
        print(course_id, "-", course_name)


store_courses(
    CS101="Introduction to Computer Science",
    MATH101="Calculus I",
    PHY101="General Physics I",
    BIO101="Biology I"
)

import tkinter as tk

def calculate():

    num1 = float(entry1.get())
    num2 = float(entry2.get())

    operation = operation_var.get()

    if operation == "Add":
        result = num1 + num2

    elif operation == "Subtract":
        result = num1 - num2

    elif operation == "Multiply":
        result = num1 * num2

    elif operation == "Divide":
        result = num1 / num2

    result_label.config(text=f"Result: {result}")


root = tk.Tk()
root.title("Calculator")

tk.Label(root, text="Number 1").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Number 2").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

operation_var = tk.StringVar()
operation_var.set("Add")

tk.OptionMenu(
    root,
    operation_var,
    "Add",
    "Subtract",
    "Multiply",
    "Divide"
).grid(row=2, column=0, columnspan=2)

tk.Button(
    root,
    text="Calculate",
    command=calculate
).grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()