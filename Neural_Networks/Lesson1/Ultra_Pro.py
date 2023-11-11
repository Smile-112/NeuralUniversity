def task_1():
    dist = 2790
    a_cost = 820
    h_cost = 110
    h_time = 6
    patrol = 15.8
    p_cost = 3.89
    dol = 77.4

    print(f"Всего будет потрачено {(dol * (a_cost + h_cost * h_time + (dist / patrol * p_cost))):.2f} рублей")


def task_2():
    a = [3, 124, 0.45, 'привет', {'ребята': 2}, 31.4, 'люди', 34, (12, 44)]
    a_1 = [index_i for index_i, i in enumerate(a) if not (type(i) == int or type(i) == float)]
    a_2 = [i for i in a if (type(i) == int or type(i) == float)]
    print(a_1)
    print(a_2)


def task_3():
    player_1 = [6, 10, 7, 8, 9, 6]
    player_2 = [10, 7, 9, 6, 10, 7]

    for i in range(6):
        if player_1[i] > player_2[i]:
            player_1.append(player_2[i])
        else:
            player_2.append(player_1[i])
    if sum(player_1) > sum(player_2):
        print("Победил игрок №1")
    else:
        print("Победил игрок №2)")


def task_4():
    istr = "Вставай на лыжи".upper()  # Или input("Введите три слова через пробел")
    st_2 = ""
    for i in range(len(istr) - 1):
        st_2 += istr[i]
        if not ((istr[i] == " ") or (istr[i + 1] == " ")):
            st_2 += "-"
    print("{0}{1}".format(st_2, istr[-1]))


def task_5():
    a = ["H", 1, "H", 2, "H", 3, "H"]
    if not (a.count(1) < 2 and a.count(2) < 2 and a.count(3) < 2 and a.count(4) < 2):
        print("Повторяющиеся комнаты")
        return
    for i in range(1, len(a)):
        if not ((str(a[i - 1]).isdigit() and a[i] == "H") or (a[i - 1] == "H" and str(a[i]).isdigit())):
            print("Некорректный маршрут")
            return
    print("Маршрут корректен")


# task_1()

# task_2()

# task_3()

# task_4()

# task_5()
