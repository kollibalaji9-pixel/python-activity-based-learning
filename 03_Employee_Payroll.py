print("EMPLOYEE PAYROLL SYSTEM")

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime payment: "))
incentive = float(input("Enter incentive: "))

if basic < 0 or allowance < 0 or overtime < 0 or incentive < 0:
    print("Invalid salary details")
else:
    gross = basic + allowance + overtime + incentive

    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 40000:
        deduction = gross * 0.10
    else:
        deduction = gross * 0.15

    net_salary = gross - deduction

    print("\nSALARY STATEMENT")
    print("-------------------------")
    print("Employee Name:", name)
    print("Basic Salary: Rs.", basic)
    print("Allowances: Rs.", allowance)
    print("Overtime: Rs.", overtime)
    print("Incentive: Rs.", incentive)
    print("Gross Salary: Rs.", gross)
    print("Deduction: Rs.", deduction)
    print("Net Salary: Rs.", net_salary)
