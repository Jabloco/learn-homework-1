"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main(input_age):
    try:
        age = int(input_age)
    except ValueError as error:
        print('Возраст введен не верно ', error)  
    else:    
        
        if 0 < age <= 6:
            print('Детский сад')
        elif 6 < age <= 17:
            print('Школа')
        elif 17 < age <= 23:
            print('ВУЗ')
        else:
            print('Работа')
        

if __name__ == "__main__":
  age = input('Введите возраст: ')
  main(age)
