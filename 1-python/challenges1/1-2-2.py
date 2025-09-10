
positive_count = 0
negative_count = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break
    elif num > 0:
        positive_count += 1
    else:
        negative_count += 1

print("Number of positive numbers entered:", positive_count)
print("Number of negative numbers entered:", negative_count)
