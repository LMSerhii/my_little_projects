#! python3

# phoneAndEmail.py - находит телефонные номера
# и адреса электронной почты в буфере обмена и копирует их обратно в буфер обмена.

import pyperclip
import re


def phone_ua_regex():
    # +380993041386 # +380 (97) 629-03-48 # 095 488 77 27
    # Создаем регулярное выражение
    phoneUaRegex = re.compile(r'''(
    (\+380)?                                        # Код региона   #1
    (\s|-)?                                         # Разделитель   #2
    (\(\d{2}\)|\(\d{3}\))                              # Код оператора #3
    (\s|-)?                                         # Разделитель   #4
    (\d{3})                                         # Еще 3 цифры   #5
    (\s|-)?                                         # Разделитель   #6
    (\d{2})                                         # Еще 2 цифры   #7
    (\s|-)?                                         # Разделитель   #8
    (\d{2})                                         # Еще 2 цифры   #9
    )''', re.VERBOSE)

    # записываем данные из буфера обмена в переменную
    text = str(pyperclip.paste())



    matches = []

    for groups in phoneUaRegex.findall(text):
        phoneNum = ' '.join([groups[1], groups[3], groups[5],
                             groups[7], groups[9]])
        matches.append(phoneNum)

    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Скопировано в буфер обмена:')
        print('\n'.join(matches))
    else:
        print('Телефонные номера не обнаружены.')


# ----------------------------------------------------------------------------------------------------------------------

def email_regex():

    emailRegex = re.compile(r'''
    (
    [a-zA-Z0-9._%+-]+           # имя пользователя
    @                           # символ @
    [a-zA-Z0-9.-]+              # домен
    ( \.[a-zA-Z]{2,4}  )        # остальная часть адреса
    )
    ''', re.VERBOSE)
    text = str(pyperclip.paste())       # получает строку, хранящуюся в буфере обмена


    matches = []

    for groups in emailRegex.findall(text):
        matches.append(groups[0])


    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Скопировано в буфер обмена:')
        print('\n'.join(matches))
    else:
        print('Адреса электронной почты не обнаружены.')


def main():
    phone_ua_regex()
    # email_regex()


if __name__ == "__main__":
    main()

