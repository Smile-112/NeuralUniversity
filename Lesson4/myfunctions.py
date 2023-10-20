def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    """
    return "**********"


print(f"Функция simple_separator: "
      f"{simple_separator() == '**********'}")  # True


def long_separator(count):
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    return "*" * count


print(f"Функция long_separator: "
      f"{long_separator(3) == '***'} и "
      f"{long_separator(4) == '****'}")  # True


def separator(simbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    return simbol * count

print(f"Функция separator: "
      f"{separator('-', 10) == '----------'} и "
      f"{separator('#', 5) == '#####'}")


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    print("********\n\nHello World!\n\n########\n")


'''
**********

Hello World!

##########
'''
print("Функция hello_world!")
hello_world()



def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    print(f"********\n\nHello {who}!\n\n########\n")


print("Функция hello_who:")
hello_who()
'''
**********

Hello Max!

##########
'''
hello_who('Max')
'''
**********

Hello Kate!

##########
'''
hello_who('Kate')


def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    sum = 0
    for i in args:
        sum += i
    return sum**power


print(f"Функция pow_many: "
      f"{pow_many(1, 1, 2) == 3}, "
      f"{pow_many(1, 2, 3) == 5}, "
      f"{pow_many(2, 1, 1) == 4}, "
      f"{pow_many(3, 2) == 8}, "
      f"{pow_many(2, 1, 2, 3, 4) == 100}\n")

def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, value in kwargs.items():
        print(f"{key} --> {value}")
    print()

"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    return list(filter(function, iterable))


print(f"Функция my_filter: "
      f"{my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5]}, "
      f"{my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2]}, "
      f"{my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5]}, "
      f"{my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b']}")
