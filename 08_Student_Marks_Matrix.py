print("STUDENT MARKS MATRIX ANALYSIS")

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Invalid number of students or subjects")
else:
    marks = []
    valid_input = True

    for i in range(students):
        row = []
        print("\nStudent", i + 1)
        for j in range(subjects):
            mark = float(input("Enter subject " + str(j + 1) + " marks: "))
            if mark < 0 or mark > 100:
                print("Invalid marks. Marks must be between 0 and 100.")
                valid_input = False
                break
            row.append(mark)
        if not valid_input:
            break
        marks.append(row)

    if valid_input:
        totals = []
        print("\nSTUDENT RESULTS")

        for i in range(students):
            total = sum(marks[i])
            average = total / subjects
            totals.append(total)
            print("Student", i + 1)
            print("Marks:", marks[i])
            print("Total:", total)
            print("Average:", round(average, 2))

        topper = totals.index(max(totals))
        print("\nTop Performer: Student", topper + 1)
        print("Highest Total:", max(totals))

        print("\nSUBJECT AVERAGES")
        for j in range(subjects):
            subject_total = 0
            for i in range(students):
                subject_total += marks[i][j]
            print("Subject", j + 1, "Average:",
                  round(subject_total / students, 2))
