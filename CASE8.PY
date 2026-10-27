material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))
wastage = float(input("Enter wastage cost: "))

quantity = int(input("Enter number of products: "))
selling_price = float(input("Enter selling price per product: "))
target = float(input("Enter target profit: "))

cost = material + labour + machine + wastage
revenue = quantity * selling_price
profit = revenue - cost

print("Total production cost:", cost)
print("Total revenue:", revenue)
print("Profit:", profit)

if profit >= target:
    print("Profit target achieved")
else:
    print("Profit target not achieved")