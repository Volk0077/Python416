# import re

"""
print(re.findall(r'\w+', '12 + й'))
print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

text = 'Hello World'
print(re.findall(r'\w+', text))
"""


# Рекурсия --------------------------------------------------------------------

"""
def sum_list(lst):
    res = 0
    for i in lst:
        res += i
    return res
"""

# Задача сверху только в рекурсии
"""
def sum_list(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])


print(sum_list([1, 3, 5, 7, 9]))

"""
"""
def to_str(n, base):
    convert = '0123456789'
    if n < base:
        return convert[n]
    else:
        return to_str(n // base, base) + convert[n % base]
"""


names = [
    "Adam",
    ["Bob", ["Chet", "Cat"], "Bard", "Bert"],
    "Alex",
    ["Bea", "Bill"],
    "Ann",
]
# print(names)
# print(len(names))

# print(names[1][1])


def count_items(item_list):
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_items(item)
        else:
            count += 1
    return count


print(count_items(names))
