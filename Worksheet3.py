# Student Course Enrollment
course_enrollments = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101", "MATH102"],
    1003: ["CS202", "PHY101"],
    1004: ["CS202", "CHEM101"]
}

# Loop and print
for student_id, courses in course_enrollments.items():
    print(f"Student ID {student_id} is enrolled in: {', '.join(courses)}")
    departments = {
    "Computer Science": [("CS101", "Intro to CS"), ("CS202", "Data Structures")],
    "Mathematics": [("MATH101", "Calculus I"), ("MATH102", "Calculus II")],
    "Physics": [("PHY101", "Physics I")]
}

for dept, courses in departments.items():
    print(f"\nDepartment: {dept}")
    for course in courses:
        print(f"{course[0]} - {course[1]}")
        lecturer_assignments = {
    "Dr John": ["CS101", "MATH102"],
    "Prof Jane": ["PHY101"],
    "Mr Mike": ["CS202", "CHEM101"]
}

for lecturer, courses in lecturer_assignments.items():
    print(f"{lecturer} teaches: {', '.join(courses)}")

students = ["Tenzin", "Norphel", "Dorji"]

for student in students:
    print(f"{student} has been added to the class.")

print("\nFinal Student List:")
for student in students:
    print(student)

print("Total students:", len(students))
rooms = [
    [101, 15, "Ground Floor", "Building A"],
    [102, 15, "Ground Floor", "Building A"],
    [103, 20, "Ground Floor", "Building A"],
    [104, 20, "Ground Floor", "Building A"],
    [105, 25, "Ground Floor", "Building A"],
    [106, 25, "Ground Floor", "Building A"],
    [107, 30, "Ground Floor", "Building A"],
    [108, 30, "Ground Floor", "Building A"],
    [109, 30, "Ground Floor", "Building A"],
    [206, 40, "1st Floor", "Building A"]
]

students_attending = int(input("Enter number of students attending: "))

for room in rooms:
    room_number = room[0]
    capacity = room[1]
    floor = room[2]
    location = room[3]

    if capacity >= students_attending:
        print("Suitable room found:")
        print("Room Number:", room_number)
        print("Capacity:", capacity)
        print("Floor:", floor)
        print("Location:", location)
        break