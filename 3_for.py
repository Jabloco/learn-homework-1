"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main(input_classes_and_grades):
    
    total_sum = 0  # общая сумма баллов по школе
    total_grades = 0  # общее количество оценок по школе
    for grades_in_class in input_classes_and_grades:
        total_sum += sum(grades_in_class['scores'])
        total_grades += len(grades_in_class['scores'])
        class_midle_grade = round(total_sum / total_grades, 1)  # средний балл в классе
        print(f"Средний балл по {grades_in_class['school_class']} классу составляет {class_midle_grade}")
    school_midle_grade = round(total_sum / total_grades, 1)  # средний балл по школе
    print(f'Средний балл по школе {school_midle_grade}')


if __name__ == "__main__":
    classes_and_grades = [  
        {'school_class': '1a', 'scores': [4,4,2,5,5,4,3]},
        {'school_class': '1b', 'scores': [5,4,2,5,2,5,5]},
        {'school_class': '2a', 'scores': [2,4,4,5,5,4]},
        {'school_class': '2b', 'scores': [4,4,2,5,2,4]},
        {'school_class': '3a', 'scores': [5,4,4,5]},
        {'school_class': '4a', 'scores': [3,4,3,5,2]}
    ]
    
    main(classes_and_grades)
