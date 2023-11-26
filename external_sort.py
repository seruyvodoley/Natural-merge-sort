"""модуль внешней сортировки есественным слиянием"""
import argparse
import csv
from pathlib import Path


def default_key(elem):
    """
    вернуть элемент
    :param elem: элемент
    :return: элемент
    """
    return elem


def get_decim(elem):
    """
    вернуть остаток от деления на 10 от элемента
    :param elem: элемент
    :return: остаток от деления
    """
    return elem % 10


def merge(reverse, key, digit):
    """
    слияние двух последовательностей внешней сортировки

    :param reverse: флажок для сортировки по убыванию
    :param key: ключ сортировки
    :param digit: тип данных (0 - int, 1 - float, 2 - str).
    """
    src = "buffer.txt"
    seq1 = open("sequence1.txt", 'r')
    seq2 = open('sequence2.txt', 'r')
    dump = open(src, 'a')
    element1 = seq1.readline().replace("\n", '')
    element2 = seq2.readline().replace("\n", '')
    while True:
        if element1 != '' and element2 != '':
            if digit == 0:
                element1 = int(element1)
                element2 = int(element2)
            elif digit == 1:
                element1 = float(element1)
                element2 = float(element2)

        if element1 != '' and element2 != '':
            if not reverse:
                if key(element1) <= key(element2):
                    dump.write(str(element1) + '\n')
                    element1 = seq1.readline().replace("\n", '')
                else:
                    dump.write(str(element2) + '\n')
                    element2 = seq2.readline().replace("\n", '')
            else:
                if key(element1) >= key(element2):
                    dump.write(str(element1) + '\n')
                    element1 = seq1.readline().replace("\n", '')
                else:
                    dump.write(str(element2) + '\n')
                    element2 = seq2.readline().replace("\n", '')
        else:
            if element1 == '' and element2 == '':
                break
            elif element1 != '' and element2 == '':
                dump.write(str(element1) + '\n')
                element1 = seq1.readline().replace("\n", '')
            elif element2 != '' and element1 == '':
                dump.write(str(element2) + '\n')
                element2 = seq2.readline().replace("\n", '')
    seq1.close()
    seq2.close()
    dump.close()
    open('sequence1.txt', 'w').close()
    open('sequence2.txt', 'w').close()


def is_digit(src):
    """
    определение типа данных в файле

    :param src: путь к файлу
    :return: тип данных (0 - int, 1 - float, 2 - str)
    """
    with open(src, 'r') as datafile:
        flag = 0  # 0 - int, 1 - float, 2 - str
        while 1:
            element = datafile.readline().replace('\n', '')
            if element != '':
                try:
                    int(element)
                except ValueError:
                    try:
                        float(element)
                        flag = max(flag, 1)
                    except ValueError:
                        flag = 2
            else:
                break
        return flag


def read_csv(src, input_row):
    """
    чтение и запись csv столбца в txt

    :param src: путь к csv
    :param input_row: имя столбца для записи
    """
    with open(src, newline="") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        if not Path('data.txt').is_file():
            Path('data.txt').touch()
        open('data.txt', 'w').close()
        with open('data.txt', 'a') as txt_file:
            for row in reader:
                txt_file.write(row[input_row] + '\n')


def copy_from_to(from_file, to_file):
    """
    копирование из одного файла в другой

    :param from_file: путь к исходному файлу
    :param to_file: путь к выходному файлу
    """
    open(to_file, 'w').close()
    from_file = open(from_file, 'r')
    to_file = open(to_file, 'a')
    while True:
        element1 = from_file.readline().replace("\n", '')
        if element1 == "":
            break
        to_file.write(element1 + "\n")
    from_file.close()
    to_file.close()


def sorted_check(src, reverse, key, digit):
    """
    проверка сортировки файла

    :param src: путь к файлу
    :param reverse: флажок для сортировки по убыванию
    :param key: ключ сортировки
    :param digit: тип данных (0 - int, 1 - float, 2 - str).
    :return: true если отсортирован, иначе false
    """
    with open(src, 'r') as datafile:
        flag = True
        previous = ""
        while flag:
            element = datafile.readline().replace('\n', '')
            if element:
                if digit == 0:
                    element = int(element)
                elif digit == 1:
                    element = float(element)

            if element == '':
                break
            if previous == "":
                previous = element
                continue
            if not reverse:
                if key(previous) > key(element):
                    flag = False
                    continue
            else:
                if key(previous) < key(element):
                    flag = False
                    continue
            previous = element
        return flag


def copy_csv_file(from_file, to_file):
    """
    копирование из одного csv в другой

    :param from_file: путь к исходному csv
    :param to_file: путь к выходному csv
    """
    with open(from_file, newline='') as csv_source:
        with open(to_file, 'w', newline='') as csv_output:
            reader = csv.DictReader(csv_source, delimiter=',')
            writer = csv.DictWriter(csv_output, delimiter=',', fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                writer.writerow(row)


def count_rows(src):
    """
    посчитать количество строк в файле

    :param src: путь к csv файлу
    :return: количество строк в файле
    """
    with open(src, 'r', newline='') as csv_file:
        count = 0
        reader = csv.DictReader(csv_file, delimiter=',')
        for _ in reader:
            count += 1
    return count


def sort_row_in_csv(src, output, row):
    """
    сортировка по столбцу в csv

    :param src: путь к входному csv файлу
    :param output: путь к выходному csv файлу
    :param row: столбец для сортировки
    """
    tmp_csv = 'tmp.csv'
    if not Path(tmp_csv).is_file():
        Path(tmp_csv).touch()
    copy_csv_file(src, tmp_csv)
    with open(tmp_csv, 'r', newline='') as tmp_data:
        reader = csv.DictReader(tmp_data, delimiter=',')
        fieldnames = reader.fieldnames
        unique_values = list(reader)
    with open(output, 'w', newline='') as csv_output:
        writer = csv.DictWriter(csv_output, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        count = count_rows(tmp_csv)

        with open('data.txt', 'r') as datafile:
            for i in range(count):
                element = datafile.readline().replace("\n", '')
                with open(tmp_csv, 'r', newline='') as tmp_data:
                    reader = csv.DictReader(tmp_data, delimiter=',')
                    for tmp_row in reader:
                        if tmp_row[row] == element and tmp_row in unique_values:
                            unique_values.remove(tmp_row)
                            writer.writerow(tmp_row)
                            break
    if Path(tmp_csv).is_file():
        Path(tmp_csv).unlink()

def separate_and_merge(src, reverse, key, digit):
    """
    разделение и слияние файлов для внешней сортировки

    :param src: путь к входному файлу
    :param reverse: флажок для сортировки по убыванию
    :param key: ключ сортировки
    :param digit: Тип данных элементов (0 - int, 1 - float, 2 - str).
    """
    datafile = open(src, 'r')
    counter = 0
    previous = ""
    seq = list()
    seq.append(open('sequence1.txt', 'a'))
    seq.append(open('sequence2.txt', 'a'))
    flag = 0

    while True:
        element = datafile.readline().replace("\n", '')
        if element != '':
            if digit == 0:
                element = int(element)
            elif digit == 1:
                element = float(element)
        if previous == "":
            previous = element
        if element == "":
            seq[0].close()
            seq[1].close()
            merge(reverse, key, digit)
            break
        if not reverse and key(previous) > key(element):
            flag = 1
            counter += 1
        elif reverse and key(previous) < key(element):
            flag = 1
            counter += 1
        previous = element
        if counter == 2:
            seq[0].close()
            seq[1].close()
            merge(reverse, key, digit)
            seq = list()
            seq.append(open('sequence1.txt', 'a'))
            seq.append(open('sequence2.txt', 'a'))
            counter = 0
        seq[flag].write(str(element) + "\n")
    seq[0].close()
    seq[1].close()
    datafile.close()


def natural_merge(src, output=None, reverse=False, key=default_key):
    """
    естественное слияние для внешней сортировки

    :param src: путь к входным файлам
    :param output: путь к выходному файлу. если нет, то в исходный
    :param reverse: флажок для сортировки по убыванию
    :param key:  ключ сортировки
    """
    if isinstance(src, list):  # для тестов
        separator = '.'
        src = separator.join(src)
    file_format = src.split('.')[1]
    if key is None:
        key = default_key
    if output and output.split('.')[1] != file_format:
        raise TypeError('расширение входного и выходного файла разные')
    if file_format == "csv":
        row = input("введите ключ для сортировки в csv файле: ")
        read_csv(src, row)
        csv_source = src
        if output is None:
            output = src
        elif not Path(output).is_file():
            Path(output).touch()
        csv_output = output
        output = 'data.txt'
    else:
        if output is None:
            output = src
        elif not Path(output).is_file():
            Path(output).touch()
            copy_from_to(src, output)
        else:
            copy_from_to(src, output)
    digit = is_digit(output)
    buffer = 'buffer.txt'
    while True:
        open(buffer, 'w').close()
        separate_and_merge(output, reverse, key, digit)
        copy_from_to(buffer, output)
        if sorted_check(output, reverse, key, digit):
            break
    if file_format == 'csv':
        sort_row_in_csv(csv_source, csv_output, row)


if __name__ == '__main__':
    """просто мэйн"""
    parser = argparse.ArgumentParser()
    parser.add_argument("files", type=str, nargs='+', help="файлы для сортировки")
    parser.add_argument("-o", type=str, default=None, help='файл для результата')
    parser.add_argument("-r", action='store_true', help='сортировка по убыванию')
    parser.add_argument("--key", type=str, default=None, help='сортировка по ключу')
    arguments = parser.parse_args()
    parse_files = arguments.files
    parse_output = arguments.o
    parse_reverse = arguments.r
    parse_key = arguments.key
    if parse_key == 'get_decim':
        parse_key = get_decim
    else:
        parse_key = None
    if len(parse_files) > 1:
        parse_output = None
    continue_flag = True
    prev = ''
    for file in parse_files:
        extension = file.split('.')[1]
        if prev and extension != prev:
            continue_flag = False
        prev = extension
    for file in parse_files:
        if not Path(file).is_file():
            continue_flag = False
    if continue_flag:
        for source in parse_files:
            natural_merge(source, parse_output, parse_reverse, parse_key)
    else:
        print('не совпадают расширения\n')
