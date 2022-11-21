# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import random
import os


def get_data():
    # parse date from the site
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/103.0.0.0 Safari/537.36"
    }

    url = "https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_\
    %D1%81%D1%82%D0%BE%D0%BB%D0%B8%D1%86%D1%8C_%D0%BA%D1%80%D0%B0%D1%97%D0%BD_%D1%81%D0%B2%D1%96%D1%82%D1%83"

    req = requests.get(url=url, headers=headers)

    with open("index_text.html", "w", encoding='utf-8') as file:
        file.write(req.text)


def find_elements():

    # We find countries and their capitals
    with open("index_text.html", "r", encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, 'html.parser')
    countries = soup.find(class_="wikitable sortable mw-collapsible")
    trs = countries.find_all("tr")

    # we are creating a dictionary with countries and their capitals
    countries = {}
    for tr in trs[1:]:
        all_td = tr.find_all("a")
        country = all_td[2].text
        capital = all_td[0].text
        countries[country] = capital

    return countries



def create_questions(countries):

    # based on the dictionary, we create files with questions and answer options

    for quiz_num in range(1, 36):

        # if there is no directory, we create it
        if not os.path.exists("QUIZ"):
            os.mkdir("QUIZ")

        # at each iteration, we create a text file with
        # ticket number for questions
        with open(f"QUIZ/capital_quiz_{quiz_num}.txt", "w", encoding='utf-8') as file:
            file.write("І'мя:\n\nДата:\n\nГруппа:\n\n")
            file.write((" " * 20) + f'Столиці країн (квиток {quiz_num})')
            file.write("\n\n")

       # create a text file with the correct answers
        with open(f"QUIZ/capitals_quiz_answers_{quiz_num}.txt", "w", encoding='utf-8') as file:
            file.write('Відповіді\n')

        # we create a list with dictionary keys (regions) and shuffle it
        capitals = list(countries.keys())
        random.shuffle(capitals)

        for question_num in range(181):
            # we create correct and incorrect answers
            correct_answer = countries[capitals[question_num]]

            wrong_answers = list(countries.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            wrong_answers = random.sample(wrong_answers, 3)

            answer_options = wrong_answers + [correct_answer]
            random.shuffle(answer_options)

            # add answer options to the file
            with open(f"QUIZ/capital_quiz_{quiz_num}.txt", "a", encoding='utf-8') as file:
                file.write(f'{question_num+1}. Виберіть адміністративний центр області {capitals[question_num]}.\n')

            for i in range(4):

                with open(f"QUIZ/capital_quiz_{quiz_num}.txt", "a", encoding='utf-8') as file:
                    file.write('\n')
                    file.write(f"    {'АБВГ'[i]}.  {answer_options[i]}\n")
                    file.write('\n')

            with open(f"QUIZ/capitals_quiz_answers_{quiz_num}.txt", "a", encoding='utf-8') as file:
                file.write(f"{question_num + 1}. {'АБВГ'[answer_options.index(correct_answer)]}\n")


def main():
    # get_data()
    countries = find_elements()
    create_questions(countries=countries)


if __name__ == "__main__":
    main()
