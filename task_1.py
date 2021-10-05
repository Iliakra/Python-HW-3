""" Красильников Илья
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_div_func(arg_1, arg_2):
    try:
        result = arg_1 / arg_2
    except ZeroDivisionError:
        return 'На 0 делить нельзя!'
    return result


num_1 = float(input("Введите делимое: "))
num_2 = float(input("Введите делитель: "))

print(my_div_func(num_1, num_2))


