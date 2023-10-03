"""

    03_legb.py
    Understanding variable scope and visibility.

"""
x = 10
list1 = [1, 2, 3]


def f1():
    # global x
    v = x * 5  # x = 20
    # print(x)
    list1.append(v)

    def f2():
        nonlocal v
        v = 30
        print(v)
    f2()
    return v


# f1()
print(x)

print()
y = f1()
print(y)
print(list1)
