budget = float(input("Enter travel budget in rupees: "))
rate = float(input("Enter exchange rate in Rs.: "))

n = int(input("Enter number of expenses: "))
total = 0
largest = 0
largest_name = ""

for i in range(n):
    name = input("Enter expense category: ")
    amount = float(input("Enter expense in foreign currency: "))

    rupees = amount * rate
    total = total + rupees

    print(name, "Cost in rupees:", rupees)

    if rupees > largest:
        largest = rupees
        largest_name = name

print("Total expenses in rupees:", total)
print("Largest expense:", largest_name)

if total <= budget:
    print("Within budget")
else:
    print("Budget exceeded")