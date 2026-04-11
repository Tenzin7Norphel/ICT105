print("Hello, world!")
a = 15
b = 12

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
c = int(a / b)
print("Value of c:", c)
print("Type of c:", type(c))

c = float(c)
print("New value of c:", c)
print("New type of c:", type(c))
message = "The result of a divided by b is "
print(message + str(c))
print("Is a greater than b?", a > b)
print("Is a equal to b?", a == b)
# ---------------------------
# SESSION 3 – LISTS
# ---------------------------

courses = [
    "Physics I", "Calculus I", "Biology I", "Data Structures and Algorithms",
    "History I", "Microeconomics", "Chemistry I", "Psychology I"
]

print("Original list:")
print(courses)

print("Sorted list:")
print(sorted(courses))

print("Reverse sorted list:")
print(sorted(courses, reverse=True))

courses.reverse()
print("Reversed list:")
print(courses)

courses.reverse()
print("Back to original:")
print(courses)

courses.sort()
print("Sorted permanently:")
print(courses)

courses.sort(reverse=True)
print("Reverse sorted permanently:")
print(courses)

courses[0] = "Linear Algebra"
print("Updated courses:")
print(courses)

courses.insert(0, "English Composition I")
courses.insert(3, "Introduction to Philosophy")
courses.append("Discrete Mathematics")

print("After adding courses:")
print(courses)

removed1 = courses.pop()
removed2 = courses.pop()
removed3 = courses.pop()
removed4 = courses.pop()

print("Removed courses:", removed1, removed2, removed3, removed4)
print("Remaining courses:", courses)


# ---------------------------
# SESSION 3 – TUPLES & LOOPS
# ---------------------------

course_tuples = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms")
]

course_names = []

for course in course_tuples:
    course_id, course_name = course
    course_names.append(course_name)

print("Course names:", course_names)


# ---------------------------
# SESSION 4 – DEPARTMENT SEARCH
# ---------------------------

departments = [
    (1, "Computer Science"),
    (2, "Mathematics"),
    (3, "Computer Science"),
    (4, "Mathematics")
]

while True:
    user_input = input("Enter course ID (1-15) or 0 to quit: ")

    if user_input == "0":
        print("Exited program.")
        break

    if not user_input.isdigit():
        print("Invalid input.")
        continue

    course_id = int(user_input)
    found = False

    for cid, dept in departments:
        if cid == course_id:
            print(f"Course ID {course_id} is in the {dept} department.")
            found = True
            break

    if not found:
        print("Course ID not found.")