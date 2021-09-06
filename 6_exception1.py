"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    
        is_good = ""
        while is_good != "Хорошо":
            try:
                print("Как дела?")
                is_good = input()
            except KeyboardInterrupt:  # перехват Ctrl + C
                print("Пока!")
                break
    
if __name__ == "__main__":
    hello_user()
