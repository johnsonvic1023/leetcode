import functools

nums = [3, 30, 34, 5, 9]


def sorted_by(x, y):
    return -1 if x + y > y + x else 1


cmp = functools.cmp_to_key(sorted_by)

result = ''.join(sorted(map(str, nums), key=cmp))

print(result)