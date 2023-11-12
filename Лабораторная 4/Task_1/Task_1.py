import json

# TODO решите задачу
def task() -> float:
    # Замените 'input.json' на имя вашего файла JSON
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычислите сумму произведений "score" * "weight" для каждого словаря
    result = sum(entry["score"] * entry["weight"] for entry in data)

    # Округлите результат до 3 знаков после запятой
    result = round(result, 3)

    return result

print(task())
