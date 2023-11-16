"""Тесты для модуля my_sort"""

import csv
import os
import unittest
import shutil

from external_sort import natural_merge as my_sort

TEST_NUMBER = [
    [],
    [1],
    [1, 2, 3, 4, 5],
    [0, 0, 0, 55, 55, 60],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    [8, 0, 42, 3, 4, 8, 0, 45, 50, 9999, 7],
    [-5, 0, 9, -999, 874, 35, -4, -5, 0],
    [1, 1, 1],
]

TEST_STR = [
    [],
    ["a"],
    ["a", "b", "c", "d", "e"],
    ["aa", "aa", "aa", "ab", "ac", "b"],
    ["e", "d", "c", "b", "a"],
    ["abc", "a", "foo", "bar", "booz", "baz", "spam", "love"],
    ["abc", "abc", "abc"],
    [""],
]

TEST_FLOAT = [
    [],
    [1.0],
    [1.0, 2.0, 3.0, 4.0, 5.0],
    [0.0, 0.0, 0.0, 55.0, 55.0, 60.0],
    [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 0.2, 0.1, 0.0],
    [8.0, 0.0, 42.0, 3.0, 4.0, 8.0, 0.0, 0.45, 0.50, 9999.0, 7.0],
    [-5.0, 0.0, 9.0, -999.0, 874.0, 35.0, -4.0, -5.0, 0.0],
    [0.1, 1.0, 0.1],
]

TEST_MORE_TXT = [
    [[], []],
    [[1], [-1000]],
    [[1, 2], [3, 4, 5]],
    [[0, 0, 0], [55, 55, 60]],
    [[9, 8, 7, 6, 5], [4, 3, 2, 1, 0]],
    [[8, 0, 42, 3, 4], [8, 0, 45, 50, 9999, 7]],
    [[-5, 0, 9, -999], [874, 35, -4, -5, 0]],
    [[1, 1], [1]],
]


class TestExternalSortOneFile(unittest.TestCase):
    """Тест-кейс модуля my_sort с одним файлом."""

    def setUp(self) -> None:
        """Создание файлов перед тестом."""
        self.file_name = "tests/test_sort_one_file.txt"
        self.dir_name = "tests"
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)
        if not os.path.exists(self.file_name):
            open(self.file_name, "x", encoding="utf-8").close()

    def test_sort_number_increase(self) -> None:
        """Тест функции сортировки числовых данных по возрастанию и txt файла."""
        for data in TEST_NUMBER:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(str(item) + "\n")
            print(self.file_name)
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output=None,
                    reverse=False,
                    key=None,
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(int(ptr.readline()))
                self.assertEqual(exit_lst, sorted(data))

    def test_sort_number_decrease(self) -> None:
        """Тест функции сортировки числовых данных по невозрастанию и txt файла."""
        for data in TEST_NUMBER:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output=None,
                    reverse=True,
                    key=None,
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(int(ptr.readline()))
                self.assertEqual(exit_lst, sorted(data, reverse=True))

    def test_sort_str_increase(self) -> None:
        """Тест функции сортировки строковых данных по возрастанию и txt файла."""
        for data in TEST_STR:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(item + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output=None,
                    reverse=False,
                    key=None,
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(ptr.readline().replace("\n", ""))
                self.assertEqual(exit_lst, sorted(data, reverse=False))

    def test_sort_str_decrease(self) -> None:
        """Тест функции сортировки строковых данных по невозрастанию и txt файла."""
        for data in TEST_STR:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output=None,
                    reverse=True,
                    key=None,
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(ptr.readline().replace("\n", ""))
                self.assertEqual(exit_lst, sorted(data, reverse=True))

    def test_sort_float_increase(self) -> None:
        """Тест функции сортировки чисел с плавающей точкой по возрастанию."""
        for data in TEST_FLOAT:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output=None,
                    reverse=False,
                    key=None,
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(float(ptr.readline()))
                self.assertEqual(exit_lst, sorted(data, reverse=False))

    def test_sort_float_decrease(self) -> None:
        """Тест функции сортировки чисел с плавающей точкой по невозрастанию."""
        for data in TEST_FLOAT:
            with open(self.file_name, "w", encoding="utf-8") as ptr:
                for item in data:
                    ptr.write(str(item) + "\n")
            with self.subTest():
                my_sort(
                    src=[self.file_name],
                    output=None,
                    reverse=True,
                    key=None,
                )
                exit_lst = []
                with open(self.file_name, "r", encoding="utf-8") as ptr:
                    for _ in range(len(data)):
                        exit_lst.append(float(ptr.readline()))
                self.assertEqual(exit_lst, sorted(data, reverse=True))


    def tearDown(self) -> None:
        """Действия после окончания теста."""
        shutil.rmtree(self.dir_name)


class TestExternalSortCSVFile(unittest.TestCase):
    """Тест-кейс модуля my_sort с csv файлами."""

    def setUp(self) -> None:
        """Создание файлов перед тестом."""
        self.file_name = "tests/test_sort_csv.csv"
        self.dir_name = "tests"
        if not os.path.exists(self.dir_name):
            os.mkdir(self.dir_name)
        if not os.path.exists(self.file_name):
            open(self.file_name, "x", encoding="utf-8").close()

    def test_sort_csv_file(self) -> None:
        """Тест функции сортировки csv файла"""
        key = "Age"  # Пример ключа для сортировки, может быть изменен
        expected_sorted_data = []

        # Читаем данные из файла и сортируем их с помощью sorted()
        with open("data.csv", "r", newline="") as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                expected_sorted_data.append(row)

        expected_sorted_data = sorted(expected_sorted_data, key=lambda x: x[key])

        # Сортируем данные с помощью my_sort, передав ключ
        my_sort(src="data.csv", output=None, reverse=False, key=None)

        # Читаем данные из отсортированного файла
        sorted_data = []
        with open("data.csv", "r", newline="") as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                sorted_data.append(row)

        # Извлекаем только ключевые значения для сравнения
        sorted_keys = [item[key] for item in sorted_data]
        expected_keys = [item[key] for item in expected_sorted_data]

        # Сравниваем отсортированные ключи
        self.assertEqual(sorted_keys, expected_keys)

    def tearDown(self) -> None:
        """Действия после окончания теста."""
        shutil.rmtree(self.dir_name)
