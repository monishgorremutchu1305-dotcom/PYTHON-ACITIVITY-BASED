usage = float(input("Enter required data in GB: "))
budget = float(input("Enter your budget: "))

plans = [
    ("Plan A", 2, 199),
    ("Plan B", 5, 299),
    ("Plan C", 10, 399)
]

best_plan = ""
lowest_cost = 999999

for name, data, price in plans:
    if data >= usage and price <= budget:
        if price < lowest_cost:
            lowest_cost = price
            best_plan = name

if best_plan != "":
    print("Best plan:", best_plan)
    print("Plan cost: Rs.", lowest_cost)
else:
    print("No suitable plan found")