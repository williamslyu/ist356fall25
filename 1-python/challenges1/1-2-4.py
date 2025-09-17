
shopping_list = {}

while True:
    item = input("Enter a grocery item (or 'quit' to stop): ").strip().lower()
    if item == "quit":
        break

    try:
        quantity = int(input(f"Enter quantity for {item}: "))
    except ValueError:
        print("Please enter a valid number for quantity.")
        continue

    if item in shopping_list:
        shopping_list[item] += quantity
    else:
        shopping_list[item] = quantity

    print("Current shopping list:", shopping_list)

print("\nFinal shopping list:")
for item, qty in shopping_list.items():
    print(f"{item}: {qty}")
