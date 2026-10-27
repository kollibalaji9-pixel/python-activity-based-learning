print("UNIVERSITY SCHOLARSHIP ALLOCATION")

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter student name: ")
    marks = float(input("Enter aggregate marks (%): "))
    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter annual family income: "))

    if marks >= 75 and attendance >= 75 and income <= 200000:
        students.append((name, marks, attendance, income))

students.sort(key=lambda x: x[1], reverse=True)

print("\nELIGIBLE STUDENTS")
if not students:
    print("No eligible students found.")
else:
    for rank, student in enumerate(students, start=1):
        name, marks, attendance, income = student
        print("Rank:", rank)
        print("Name:", name)
        print("Marks:", marks)
        print("Attendance:", attendance)
        print("Family Income:", income)
        print("-----------------------------")
