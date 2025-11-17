def sum_of_positives(numbers):
    total = 0

    for x in numbers:
        if x > 0:
         total = total + x

    return total

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is ", result)