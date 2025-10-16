print("Task 1")
# Write a function that calculates the product of the elements from a list of integers. The list is passed as a parameter.
#  The result is returned from the function.


def product_calculator(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


print(product_calculator([5, 2, 6, 1]))  # <-----trebuie sa pun lista intre ()

print("Task 2")
# Write a function to find the minimum in a list of integers. The list is passed as a parameter. The result is returned from the function.


def minimum_finder(list1):
    result = min(list1)
    return result


print(f"The smallest number is: {minimum_finder([15, 32, 12, 5, 64, 25])}")

print("Task 3")
# Write a function that determines how many prime numbers there are in the list of integers. The list is passed as a parameter.
#  The result is returned from the function.


def prime_counter(list2):
    def is_prime(n):  # <---verifica daca e prim
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
            return True

    return sum(1 for num in list2 if is_prime(num))  # returneza nr de nr primi


print(prime_counter([5, 6, 3, 7, 9, 2, 15, 23]))

print("Task 4")
# Write a function that removes a given number from the list of integers. Return the number of removed elements from the function.


def target_remover(list3, target):
    removed = list3.count(target)
    while target in list3:
        list3.remove(target)
    return removed


print(target_remover([5, 5, 3, 7, 6, 1, 78, 6, 5, 4, 4, 9, 4], 4))

print("Task 5")
# Write a function that takes two lists as a parameter and returns a list containing the elements of both lists.


def list_combiner(list4, list5):
    return list4 + list5


print(list_combiner([1, 2, 3, 4], [5, 6, 7, 8]))

print("Task 6")
# Write a function that calculates the power of each element from the list of integers.
#  A value for the power is passed as a parameter, the list is also passed as a parameter.
#  The function returns a new list containing the results.


def power_raiser(list6, power):
    return [i**power for i in list6]


print(power_raiser([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
