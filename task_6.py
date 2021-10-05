""" Красильников Илья
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(text):
    result = text.title()
    return result


print(int_func('text'))


def str_to_title(user_str):
    str_list = user_str.split()
    result_str = ""
    for el in str_list:
        result_str += int_func(el) + " "
    return result_str


print(str_to_title("privet wrf dry"))


