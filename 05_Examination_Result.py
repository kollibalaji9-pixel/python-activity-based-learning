print("EXAMINATION RESULT SYSTEM")

marks = []
subjects = int(input("Enter number of subjects: "))

if subjects <= 0:
    print("Invalid number of subjects")
else:
    valid_input = True

    for i in range(subjects):
        mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
        if mark < 0 or mark > 100:
            print("Invalid marks. Marks must be between 0 and 100.")
            valid_input = False
            break
        marks.append(mark)

    if valid_input:
        grace_used = False
        for i in range(subjects):
            if 30 <= marks[i] < 35 and not grace_used:
                marks[i] = min(100, marks[i] + 5)
                grace_used = True

        total = sum(marks)
        percentage = total / subjects

        print("\nFINAL RESULT")
        print("Subject Marks:", marks)
        print("Total Marks:", total)
        print("Percentage:", round(percentage, 2), "%")

        if min(marks) < 35:
            print("Result: FAIL")
        elif percentage >= 75:
            print("Result: DISTINCTION")
        elif percentage >= 60:
            print("Result: FIRST CLASS")
        elif percentage >= 50:
            print("Result: SECOND CLASS")
        else:
            print("Result: PASS")
