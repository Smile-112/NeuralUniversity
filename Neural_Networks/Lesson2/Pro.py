import numpy as np
import matplotlib.pyplot as plt
import random


def task_1():
    arr = np.random.randint(15, 37, (3, 4)).astype("object")
    print(arr)

    for index, x in np.ndenumerate(arr):
        if x < 20:
            arr[index] = "small"
        elif x <= 30:
            arr[index] = "medium"
        else:
            arr[index] = "large"
    print(arr)


def task_2():
    print(f"Первый понедельник в 2015 году:\n{np.busday_offset('2015', 0, roll='forward', weekmask='Mon')}")


def task_3():
    arr = np.random.randint(0, 100, 10)
    bub = 0

    print(f"Сгенерированный массив: {arr}")
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                bub = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = bub
    print(f"Отсортированный массив: {arr}")


def task_4():
    x = np.random.randint(0, 1000, 250)
    y = np.random.randint(0, 1000, 250)
    plt.scatter(x, y, c="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("График рассеяния")
    plt.show()


def task_5():
    from matplotlib.pyplot import figure
    x = [-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
    y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]
    plt.plot(x, y)
    plt.figure()

    plt.scatter(x, y)
    plt.xlim(-20, 15)
    plt.ylim(-10, 15)
    plt.figure()

    plt.plot(x, y)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Самолёт")
    plt.rcParams["figure.figsize"] = (6, 3)
    plt.show()


task_1()
task_2()
task_3()
task_4()
task_5()
