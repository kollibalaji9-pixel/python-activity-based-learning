print("ATTENDANCE RECOVERY SYSTEM")

total_classes = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))
target = float(input("Enter required attendance percentage: "))

if total_classes <= 0 or attended < 0 or attended > total_classes:
    print("Invalid attendance details")
elif target <= 0 or target > 100:
    print("Invalid target percentage")
else:
    percentage = attended / total_classes * 100
    print("Current Attendance:", round(percentage, 2), "%")

    if percentage >= target:
        print("You are already eligible.")
        print("Additional classes required: 0")
    else:
        required = 0
        while ((attended + required) /
               (total_classes + required) * 100) < target:
            required += 1

        print("Additional consecutive classes required:", required)
        final_percentage = (attended + required) / (total_classes + required) * 100
        print("Attendance after recovery:", round(final_percentage, 2), "%")
