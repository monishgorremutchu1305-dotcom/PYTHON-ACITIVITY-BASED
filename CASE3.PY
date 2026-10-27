consultation = float(input("Enter consultation charge: "))
diagnosis = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

total = consultation + diagnosis + treatment

senior = input("Is the patient a senior citizen? (yes/no): ")

if senior.lower() == "yes":
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total charges:", total)
print("Discount:", discount)
print("Final bill:", final_bill)

if final_bill >= 10000:
    print("Classification: High bill")
else:
    print("Classification: Normal bill")