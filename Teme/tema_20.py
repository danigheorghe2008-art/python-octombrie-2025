print("Task 1")
#  Create a function that returns all odd numbers in a range.
#  The function takes the beginning and the end of the range as parameters.
#  Use the generator mechanism within the function.


def odd_num(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num


print(list(odd_num(1, 20)))

print("Task 2")
#  Create a function that returns all values from a list that are not in a range specified by a user.
#  The function takes the list, the beginning and the end of the range as parameters.
#  Use the generator mechanism within the function.


def value_list(numlist, start, end):
    for value in numlist:
        if value < start or end < value:
            yield value


list1 = [1, 2, 3, 15, 23, 25, 12, 9, 20]

print(list(value_list(list1, 9, 20)))
