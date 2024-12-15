def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"Average: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"Average of empty list: {result}") #This will return 0

my_list_with_zero = [10, 0, 20, 30]
result = calculate_average(my_list_with_zero)
print(f"Average of list with zero: {result}") #This will return correct result

my_list_with_strings = [10, 20, 'thirty', 40]
result = calculate_average(my_list_with_strings) # This will cause a TypeError
print(f"Average of list with strings: {result}")