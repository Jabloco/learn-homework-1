"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
    "Как дела": "Хорошо!",
    "Что делаешь?": "Программирую",
    "Откуда ты?": "Из Матрицы",
    "Кто такой Гвидо ван Россум": "Великодушный пожизненный диктатор"
}

def ask_user(answers_dict: dict):
    print('Для выхода введите: Хватит')
    user_question = input('Пользователь: ')
    while user_question != 'Хватит':  # выход по стоп-слову 'Хватит'
        if user_question in answers_dict.keys():
            print('Программа: ', end='')
            print(answers_dict[user_question])
        else:
            print('Программа: Мне нечего сказать')
        user_question = input('Пользователь: ')
    
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
