print("ELECTRICITY BILL CALCULATOR")

units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        bill = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7

    fixed_charge = 50
    total_bill = bill + fixed_charge

    print("\nELECTRICITY BILL")
    print("Units Consumed:", units)
    print("Energy Charge: Rs.", bill)
    print("Fixed Charge: Rs.", fixed_charge)
    print("Total Bill: Rs.", total_bill)
