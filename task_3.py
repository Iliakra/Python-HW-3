""" Красильников Илья
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.
"""


def my_func(num_1, num_2, num_3):
    arg_list = [num_1, num_2, num_3]
    arg_list.sort(reverse=True)
    print(arg_list[0] + arg_list[1])


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


my_func(a, b, c)

