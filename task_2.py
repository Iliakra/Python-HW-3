""" Красильников Илья
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
 о пользователе одной строкой.
"""


def user_data(surname, name, birth_year, city, person_email, person_tel):
    print(f"name - {name}, surname - {surname}, birth - {birth_year}, live in - {city}, email - {person_email}, tel - {person_tel} ")


user_data(surname="Ivanov", name="Petr", city="Chicago", birth_year=1987, person_email="we@yu.gf", person_tel=12345)


