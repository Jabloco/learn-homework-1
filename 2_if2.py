"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(input_str_one, input_str_two):
    str_one = input_str_one
    str_two = input_str_two
    if type(str_one) is str and type(str_two) is str:
      if str_one == str_two:
        return 1
      else:
        if len(str_one) > len(str_two):
          return 2
        elif str_two == 'learn':
          return 3
    else:
      return 0
    
    
if __name__ == "__main__":
    print(main('aa', 5))  # строка и не-строка
    print(main('aa', 'aa'))  # одинаковые строки
    print(main('aabb', 'bb'))  # первая строка длинее
    print(main('aaaaa', 'learn'))  # вторая строка содержит learn

