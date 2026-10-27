basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

gross = basic + allowances + overtime + incentives

if gross <= 20000:
    deduction = gross * 0.05
else:
    deduction = gross * 0.10

net_salary = gross - deduction

print("Gross salary:", gross)
print("Deduction:", deduction)
print("Net salary:", net_salary)