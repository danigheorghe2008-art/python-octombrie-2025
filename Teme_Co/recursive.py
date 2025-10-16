def recursive_sum(a, b):
    if a == b:
        return a
    return a + recursive_sum(a + 1, b)


# 1+2+3+4+5

print(recursive_sum(1, 5))
