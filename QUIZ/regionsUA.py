# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import random
import os


def get_data():
    # parse date from the site
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/103.0.0.0 Safari/537.36"
    }

    url = "https://uk.wikipedia.org/wiki/%D0%90%D0%B4%D0%BC%D1%96%D0%BD%D1%96%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%B8%\
    D0%B2%D0%BD%D0%B8%D0%B9_%D1%83%D1%81%D1%82%D1%80%D1%96%D0%B9_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8"

    req = requests.get(url=url, headers=headers)

    with open("index_text.html", "w", encoding='utf-8') as file:
        file.write(req.text)


def find_elements():
    # We find regions and their administrative center
    with open("index_text.html", "r", encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, 'html.parser')
    adm_centr = soup.find(class_="wikitable sortable")
    trs = adm_centr.find_all("tr")

    # we are creating a dictionary with regions and their cities
    capitals = {}
    for tr in trs[1:]:
        all_td = tr.find_all("a")
        adm_centr = all_td[2].text
        name = all_td[3].text
        capitals[adm_centr] = name

    return capitals


def create_questions(capitals):

    # based on the dictionary, we create files with questions and answer options

    for quiz_num in range(1, 36):

        # if there is no directory, we create it
        if not os.path.exists("QUIZ"):
            os.mkdir("QUIZ")

        # at each iteration, we create a text file with
        # ticket number for questions
        with open(f"QUIZ/capital_quiz_{quiz_num}.txt", "w", encoding='utf-8') as file:
            file.write("І'мя:\n\nДата:\n\nГруппа:\n\n")
            file.write((" " * 20) + f'Столиці областей (квиток {quiz_num})')
            file.write("\n\n")

       # create a text file with the correct answers
        with open(f"QUIZ/capitals_quiz_answers_{quiz_num}.txt", "w", encoding='utf-8') as file:
            file.write('Відповіді\n')

        # we create a list with dictionary keys (regions) and shuffle it
        states = list(capitals.keys())
        random.shuffle(states)

        for question_num in range(27):
            # we create correct and incorrect answers
            correct_answer = capitals[states[question_num]]

            wrong_answers = list(capitals.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            wrong_answers = random.sample(wrong_answers, 3)

            answer_options = wrong_answers + [correct_answer]
            random.shuffle(answer_options)

            # add answer options to the file
            with open(f"QUIZ/capital_quiz_{quiz_num}.txt", "a", encoding='utf-8') as file:
                file.write(f'{question_num+1}. Виберіть адміністративний центр області {states[question_num]}.\n')

            for i in range(4):

                with open(f"QUIZ/capital_quiz_{quiz_num}.txt", "a", encoding='utf-8') as file:
                    file.write('\n')
                    file.write(f"    {'АБВГ'[i]}.  {answer_options[i]}\n")
                    file.write('\n')

            with open(f"QUIZ/capitals_quiz_answers_{quiz_num}.txt", "a", encoding='utf-8') as file:
                file.write(f"{question_num + 1}. {'АБВГ'[answer_options.index(correct_answer)]}\n")


def main():
    # get_data()
    capitals = find_elements()
    create_questions(capitals=capitals)


if __name__ == "__main__":
    main()
