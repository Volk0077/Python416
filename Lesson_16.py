def my_decorator(func):
    def func_wrapper():
        print("Код до функции")
        func()
        print("Код после функции")

    return func_wrapper


def func_test():
    print("Hello, I am func 'func_test'")


test = my_decorator(func_test)
test()
