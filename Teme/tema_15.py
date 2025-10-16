print("Task 1")
# You have three tuples of integers. Find elements present in all tuples.
import random

tuple1 = tuple(random.randint(1, 20) for i in range(10))
tuple2 = tuple(random.randint(1, 20) for i in range(10))
tuple3 = tuple(random.randint(1, 20) for i in range(10))

common = tuple(set(tuple1) & set(tuple2) & set(tuple3))
print(tuple1)
print(tuple2)
print(tuple3)
print(f"The numbers that are common in all 3 tuple are:{common}")


print("Task 2")
# You have three tuples of integers. Find elements unique for each list.
import random

tuple1 = tuple(random.randint(1, 10) for i in range(5))
tuple2 = tuple(random.randint(1, 10) for i in range(5))
tuple3 = tuple(random.randint(1, 10) for i in range(5))

unique1 = tuple(
    set(tuple1) - set(tuple2) - set(tuple3)
)  # set - = elimină elementele lui tuple2 din tuple1, apoi elimină elementele lui tuple3 din rezultat.
unique2 = tuple(
    set(tuple2) - set(tuple1) - set(tuple3)
)  # Practic: toate elementele care sunt în tuple1, dar nu în tuple2 și nici în tuple3.
unique3 = tuple(set(tuple3) - set(tuple1) - set(tuple2))
print(tuple1)
print(tuple2)
print(tuple3)
print(f"The elements unique for each list 1:{unique1}")
print(f"The elements unique for each list 2:{unique2}")
print(f"The elements unique for each list 3:{unique3}")


print("Task 3")
# You have three tuples of integers. Find elements that are present in each tuple and at the same position in each tuple.
import random

tuple1 = tuple(random.randint(1, 10) for i in range(5))
tuple2 = tuple(random.randint(1, 10) for i in range(5))
tuple3 = tuple(random.randint(1, 10) for i in range(5))
print(tuple1)
print(tuple2)
print(tuple3)
same_position = tuple(
    tuple1(i)
    for i in range(min(len(tuple1), len(tuple2), len(tuple3)))
    if tuple1 == tuple2 == tuple3
)
print(
    f"elements that are present in each tuple and at the same position in each tuple:{same_position}"
)
