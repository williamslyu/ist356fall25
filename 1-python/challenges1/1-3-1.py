
def average(numbers):
    if len(numbers) == 0:   
        return 0
    return sum(numbers) / len(numbers)


my_list = [10, 20, 30, 40, 50,31]

print("List:", my_list)
print("Average:", average(my_list))
