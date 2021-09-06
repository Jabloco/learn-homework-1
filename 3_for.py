"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main(input_list):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    total_sum = 0  # общая сумма баллов по школе
    total_grades = 0  # общее количество оценок по школе
    for dict in input_list:
        total_sum += sum(dict['scores'])
        total_grades += len(dict['scores'])
        print(f"Средний балл по {dict['school_class']} классу составляет {round(sum(dict['scores']) / len(dict['scores']), 1)}")
    print(f'Средний балл по школе {round(total_sum / total_grades, 1)}')

if __name__ == "__main__":
    list_of_dict = [  
        {'school_class': '1a', 'scores': [4,4,2,5,5,4,3]},
        {'school_class': '1b', 'scores': [5,4,2,5,2,5,5]},
        {'school_class': '2a', 'scores': [2,4,4,5,5,4]},
        {'school_class': '2b', 'scores': [4,4,2,5,2,4]},
        {'school_class': '3a', 'scores': [5,4,4,5]},
        {'school_class': '4a', 'scores': [3,4,3,5,2]}
    ]
    
    main(list_of_dict)
