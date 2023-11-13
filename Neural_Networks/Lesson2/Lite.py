import numpy as np
import matplotlib.pyplot as plt


def task_1():
    arr = np.random.randint(0, 15, 10)
    arr1 = np.random.randint(0, 15, 4)
    print(np.in1d(arr, arr1))  # Или print(np.in1d(np.random.randint(0, 15, 10), np.random.randint(0, 15, 4)))


def task_2(x: int, y: int):
    print(np.arctan(y / x) if x > 0 else np.arctan(y / x) + np.pi, np.sqrt(pow(x, 2) + pow(y, 2)))


def task_3():
    arr = np.zeros((7, 7), int)
    arr = [[1, 0, 0, 1, 0, 0, 1],
           [0, 1, 0, 1, 0, 1, 0],
           [0, 0, 1, 1, 1, 0, 0],
           [1, 1, 1, 1, 1, 1, 1],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 1, 0, 1, 0, 1, 0],
           [1, 0, 0, 1, 0, 0, 1]]
    a = plt.imshow(arr)
    plt.show()


def task_4():
    programmingLanguages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [14, 13.4, 7.1, 19.1, 13.3, 2.8]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    plt.pie(popularity, labels=programmingLanguages, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.show()


def task_5():
    x = np.linspace(-100, 100, 25)
    y1 = pow(x, 3) / 100
    y2 = pow(x, 2)

    plt.plot(x, y1, linestyle="--")
    plt.plot(x, y2, linestyle="-.")
    plt.title('Графики функций y1 = x^3/100 и y2 = x^2', fontsize=12)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(["x^3/100", "x^2"], loc="lower right")
    plt.show()


task_1()
task_2(4, 3)
task_3()
task_4()
task_5()
