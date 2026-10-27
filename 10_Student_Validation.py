print("STUDENT EMAIL AND ID VALIDATION")

email = input("Enter student email: ")
student_id = input("Enter registration ID: ")

# Simplified email validation
email_valid = True

if email.count("@") != 1 or " " in email:
    email_valid = False
else:
    parts = email.split("@")
    if parts[0] == "" or parts[1] == "":
        email_valid = False
    elif "." not in parts[1]:
        email_valid = False
    elif parts[1].startswith(".") or parts[1].endswith("."):
        email_valid = False
    elif ".." in email:
        email_valid = False

# Registration ID: exactly 10 alphanumeric characters
id_valid = len(student_id) == 10

if id_valid:
    for character in student_id:
        if not character.isalnum():
            id_valid = False
            break

print("\nVALIDATION REPORT")
print("Email:", "Valid" if email_valid else "Invalid")
print("Registration ID:", "Valid" if id_valid else "Invalid")
