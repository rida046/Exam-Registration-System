print("===== EXAM REGISTRATION SYSTEM =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
course = input("Enter course name: ")
semester = input("Enter semester: ")
exam = input("Enter exam name: ")
subjects = input("Enter registered subjects: ")

print("\n===== REGISTRATION DETAILS =====")
print("Student Name:", name)
print("Roll Number:", roll_no)
print("Course:", course)
print("Semester:", semester)
print("Exam:", exam)
print("Subjects:", subjects)

with open("details.txt", "a") as file:
    file.write(
        f"{name}, {roll_no}, {course}, {semester}, {exam}, {subjects}\n"
    )

print("\nExam registration successful!")
print("Details saved successfully!")