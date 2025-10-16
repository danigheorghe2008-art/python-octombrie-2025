#  Task
#  Two lists of integers are filled with random numbers. Do the following:
#     • Create the third list containing elements of both lists;
#     • Create the third list containing elements of both lists without repetitions;
#     • Create the third list containing elements common to both lists;
#     • Create the third list containing elements that are unique to each list;
#     • Create the third list containing only the smallest and the largest values of each list.

import random

list1 = tuple(random.randint(1, 20) for i in range(5))
list2 = tuple(random.randint(1, 20) for i in range(5))

print(f"List 1:{list1}")
print(f"List 2:{list2}")

# • Create the third list containing elements of both lists;

list3_all = list1 + list2
print(f"List 3 containing elements of both lists:{list3_all}")

# • Create the third list containing elements of both lists without repetitions;

list3_norep = list(set(list3_all))
print(f"List 3 without repetitions:{list3_norep}")

# • Create the third list containing elements common to both lists;

list3_com = list(set(list1) & set(list2))
print(f"list 3 containing elements common to both lists:{list3_com}")

# • Create the third list containing elements that are unique to each list;

list3_dif = list(set(list1) ^ set(list2))
print(f"list 3 containing elements that are unique to each list:{list3_dif}")

# • Create the third list containing only the smallest and the largest values of each list.

list3_mmvalue = [min(list1), max(list1), min(list2), max(list2)]
print(
    f"list 3 containing only the smallest and the largest values of each list:{list3_mmvalue}"
)
