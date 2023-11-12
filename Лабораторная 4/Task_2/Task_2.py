import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def csv_to_json(input_filename: str, output_filename: str) -> None:
    # Чтение CSV файла и преобразование в JSON
    with open(input_filename, 'r') as csv_file:
        # Чтение CSV файла с использованием csv.DictReader
        csv_reader = csv.DictReader(csv_file)

        # Преобразование данных в список словарей
        data = [row for row in csv_reader]

    # Сериализация в JSON с отступами
    with open(output_filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def task() -> None:
    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    # Печать содержимого JSON файла
    with open(OUTPUT_FILENAME, 'r') as output_file:
        for line in output_file:
            print(line, end="")
