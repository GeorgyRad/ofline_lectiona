"""Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле."""

import sys,os

def make_directory():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(),'{} {}'.format('dir_',i))
        os.mkdir(new_path)

def remove_directory():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(),'{} {}'.format('dir_',i))
        os.rmdir(new_path)

make_directory()
remove_directory()
