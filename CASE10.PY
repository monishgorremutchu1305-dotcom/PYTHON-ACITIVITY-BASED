venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per student: "))

total_cost = venue + equipment + catering + transport + certificates

remaining = total_cost - sponsorship

if remaining < 0:
    remaining = 0

print("Total event cost:", total_cost)
print("Sponsorship:", sponsorship)
print("Remaining amount:", remaining)

if fee > 0:
    students = int(remaining / fee)

    if students * fee < remaining:
        students = students + 1

    print("Minimum registrations needed:", students)
else:
    print("Registration fee must be greater than zero")