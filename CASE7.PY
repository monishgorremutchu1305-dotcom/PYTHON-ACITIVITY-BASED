n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total = total + amount

    print(name, "Amount:", amount)

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("\nTotal amount:", total)
print("Discount:", discount)
print("Final bill:", final_bill)