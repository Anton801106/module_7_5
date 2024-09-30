# Домашнее задание по теме "Файлы в операционной системе".

import os
import time

directory = '.'  # r'C:\pythonWW\Модуль №7\ Работа с файлами и форматированный вывод\module_7_5.py'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f' Обнаружен: {file}, Путь {filepath}: , Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директоря: {parent_dir}')
