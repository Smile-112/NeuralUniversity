import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint


def task_1():
    a = np.random.randint(0, 5, (3, 4))

    b = np.random.randint(0, 5, (4, 3))

    c = np.random.randint(0, 5, (3, 3))

    print(f"Матрица а: \n{a}")
    print(f"\nМатрица b: \n{b}")
    print(f"\nМатрица c: \n{c}")

    m = len(a)
    n = len(b)
    k = len(b[0])

    d = [[None for __ in range(k)] for __ in range(m)]

    for i in range(m):
        for j in range(k):
            d[i][j] = sum(a[i][kk] * b[kk][j] for kk in range(n))

    print("\nРезультат перемножения матриц a x b = d:")
    pprint(d, width=20)
    print(f"\nПроверка:\n{a @ b}")

    m = len(d)
    n = len(c)
    k = len(c[0])

    e = [[None for __ in range(k)] for __ in range(m)]
    for i in range(m):
        for j in range(k):
            e[i][j] = sum(d[i][kk] * c[kk][j] for kk in range(n))

    print("\nРезультат перемножения матриц d x с = e:")
    pprint(e, width=20)
    print(f"\nПроверка:\n{a @ b @ c}")


def task_2(n: int):
    dx, dy = 1, 0
    x, y = 0, 0
    arr = [[None] * n for _ in range(n)]
    for i in range(1, n ** 2 + 1):
        arr[x][y] = format(i, "2")
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    for x in list(zip(*arr)):
        print(*x)


def task_3():
    print(
        f"Количество будних дней в феврале 2015 года: \n{np.busday_count('2015-02', enddates='2015-03-01', weekmask=[1, 1, 1, 1, 1, 0, 0])}")


def task_4():
    y = np.full(10, 3.0)
    patterns = ["|", "\\", "/", "+", "-", ".", "*", "x", "o", "O"]

    fig = plt.figure()
    f = fig.add_subplot(111)
    for i in range(len(patterns)):
        f.bar(i, y, color="red", edgecolor="white", hatch=patterns[i])
    plt.show()


def task_5():
    x = np.random.random(150)
    y = np.random.random(150)
    size = np.random.randint(0, 50, 150)
    color = np.random.randint(0, 100, 150)
    plt.scatter(x,y,s= size*10, c=color, alpha=0.85)
    plt.show()

task_1()
task_2(6)
task_3()
task_4()
task_5()
