def avg(fn):
    def wrap(*args):
        print("Среднее арифметическое:", *args, "=", fn(*args) / len(args))

    return wrap


@avg
def summa(*args):
    print("Сумма чисел:", *args, "=", sum(args))
    return sum(args)


summa(2, 3, 3, 4)
