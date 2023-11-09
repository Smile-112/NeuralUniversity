import os
import shutil
from Python_Developer.Lesson4.use_functions import main1 as l4_main



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
os_info()

l4_main()
