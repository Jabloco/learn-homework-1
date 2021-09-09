"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
    except (ValueError, TypeError) as error:
        return f'Что-то пошло не так: {error}'

    if discount >= max_discount:
        return price
    
    return price - (price * discount / 100)


if __name__ == "__main__":
    print(discounted(777, 150))
    print(discounted(100, -50, -105))
    print(discounted(100, 15))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(10, "десять"))
    print(discounted(100.0, 5, "10"))
    print(discounted([0, 1], 3, -105))
    
