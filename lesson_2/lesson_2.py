import csv
import json
import os
import re

import yaml


def get_data():
    """Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
    данными, их открытие и считывание данных. В этой функции из считанных данных
    необходимо с помощью регулярных выражений извлечь значения параметров
    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
    каждого параметра поместить в соответствующий список. Должно получиться четыре
    списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
    функции создать главный список для хранения данных отчета — например, main_data
    — и поместить в него названия столбцов отчета в виде списка: «Изготовитель
    системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов
     также оформить в виде списка и поместить в файл main_data (также для
    каждого файла);"""

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in os.listdir():
        if 'info_' in i:
            with open(i, 'r') as f:
                data = f.read()

                os_prod = re.search(r'(Изготовитель системы:)( +)([A-Z]+)', data)
                os_prod_list.append(os_prod.group(3))

                os_name = re.search(r'(Название ОС:)( +)(.+)', data)
                os_name_list.append(os_name.group(3))

                os_code = re.search(r'(Код продукта:)( +)(.+)', data)
                os_code_list.append(os_code.group(3))

                os_type = re.search(r'(Тип системы:)( +)(.+)', data)
                os_type_list.append(os_type.group(3))

    main_data.append(['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'])

    for i in range(len(os_prod_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i], ])

    return main_data


def write_to_csv(file_name):
    """ Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
    функции реализовать получение данных через вызов функции get_data(), а также
    сохранение подготовленных данных в соответствующий CSV-файл;
    """

    with open(file_name, 'w', encoding='utf-8') as f:
        f_writer = csv.writer(f)
        for row in get_data():
            f_writer.writerow(row)


def write_order_to_json(item, quantity, price, buyer, date):
    """Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
    (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
    должна предусматривать запись данных в виде словаря в файл orders.json. При
    записи данных указать величину отступа в 4 пробельных символа;"""

    with open('orders.json', 'r') as f:
        data = json.load(f)

    data.append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})
    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def write_yaml():
    """Подготовить данные для записи в виде словаря, в котором первому ключу
    соответствует список, второму — целое число, третьему — вложенный словарь, где
    значение каждого ключа — это целое число с юникод-символом, отсутствующим в
    кодировке ASCII (например, €);

    Реализовать сохранение данных в файл формата YAML — например,
    в файл file.yaml. При этом обеспечить стилизацию файла с помощью
    параметра default_flow_style, а также установить возможность работы
    с юникодом: allow_unicode = True;

    Реализовать считывание данных из созданного файла и проверить,
    совпадают ли они с исходными.
    """

    data = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
            'items_quantity': 4,
            'items_ptice': {'computer': '200€-1000€',
                            'printer': '100€-300€',
                            'keyboard': '5€-50€',
                            'mouse': '4€-7€'}
            }

    with open('file.yaml', 'w', encoding='utf-8') as f_in:
        yaml.dump(data, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open("file.yaml", 'r', encoding='utf-8') as f_out:
        DATA_OUT = yaml.load(f_out, Loader=yaml.SafeLoader)

    print(data == DATA_OUT)


# write_to_csv('filename.csv')
# write_order_to_json('printer', '10', '6700', 'Ivanov I.I.', '24.09.2017')
# write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')
# write_order_to_json('computer', '5', '40000', 'Sidorov S.S.', '2.05.2019')
# write_yaml()
