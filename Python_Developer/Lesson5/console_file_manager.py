import os
import shutil
from Python_Developer.Lesson4.use_functions import main1 as l4_main
from Python_Developer.Lesson3.victory import question_game as qv


def create_folder(name):
    os.mkdir(name)


def remove(path):
    if os.path.isfile(path) and os.path.exists(path):
        os.remove(path)
    elif os.path.isdir(path) and os.path.exists(path):
        os.rmdir(path)
    else:
        print("Проверьте указанный путь!")


def copy(path, dest_path):
    if os.path.exists(path) and os.path.exists(dest_path):
        shutil.copy(path, dest_path)


def contain(path):
    if os.path.exists(path):
        print(os.listdir(path))


def contain_dir(path):
    if os.path.exists(path):
        print([dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))])


def contain_file(path):
    if os.path.exists(path):
        print([dir for dir in os.listdir(path) if os.path.isfile(os.path.join(path, dir))])


def os_info():
    list = ["COMPUTERNAME", "NUMBER_OF_PROCESSORS", "OS", "PROCESSOR_ARCHITECTURE"]
    for i in list:
        print(f"{list[list.index(i)]}: {os.environ[i]}")


def change_directory(path):
    if os.path.exists(path):
        os.chdir(path)
    else:
        print("Ошибка в указании пути")


contain_file("/")

print("""
1.  создать папку;
2.  удалить (файл/папку);
3.  копировать (файл/папку);
4.  просмотр содержимого рабочей директории;
5.  посмотреть только папки;
6.  посмотреть только файлы;
7.  просмотр информации об операционной системе;
8.  создатель программы;
9.  играть в викторину;
10. мой банковский счет;
11. смена рабочей директории;

0. Выход  (ну или что угодно кроме 1-11)""")

while True:
    match int("".join([i for i in input("\nВыберите пункт из меню: ") if i.isdigit()])):
        case 1:
            name = input("Введите имя папки: ")
            create_folder(name)
            print(f"Папка создана: ")
        case 2:
            path = input("Введите путь до папки: ")
            remove(path)
            print(f"Папка на пути {path} удалена!")
        case 3:
            path = input("Введите путь до папки: ")
            dest = input("Введите конечный путь: ")
            copy(path, dest)
        case 4:
            path = input("Введите путь до папки: ")
            print(f"Содержимое папки на пути {path}: \n")
            contain(path)
        case 5:
            path = input("Введите путь до папки: ")
            print(f"Содержимое папки на пути {path} (папки):\n")
            contain_dir(path)
        case 6:
            path = input("Введите путь до папки: ")
            print(f"Содержимое папки на пути {path} (файлы):\n")
            contain_file(path)
        case 7:
            os_info()
        case 8:
            print("Здравствуйте, с Вами Smile_112.\nЕсли это автопроверка - жаль. Если же куратор - хорошего вам дня)")
        case 9:
            l4_main()
        case 10:
            qv()
        case 11:
            path = input("Введите новую рабочую директорию: ")
            change_directory(path)
        case _:
            break
